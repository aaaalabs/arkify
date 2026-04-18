const { chromium } = require('playwright');

(async () => {
  console.log('Launching browser...');
  const browser = await chromium.launch();
  const context = await browser.newContext();

  // Desktop screenshot
  console.log('Capturing desktop screenshot...');
  const desktopPage = await context.newPage();
  await desktopPage.setViewportSize({ width: 1920, height: 1080 });
  await desktopPage.goto('https://arkify.app', { waitUntil: 'networkidle' });

  // Wait for potential animations/images to load
  await desktopPage.waitForTimeout(3000);

  await desktopPage.screenshot({
    path: 'output/qa-desktop.png',
    fullPage: true
  });
  console.log('Desktop screenshot saved to output/qa-desktop.png');

  // Get console logs
  const consoleLogs = [];
  desktopPage.on('console', msg => {
    consoleLogs.push({
      type: msg.type(),
      text: msg.text()
    });
  });

  // Check for errors
  const pageErrors = [];
  desktopPage.on('pageerror', error => {
    pageErrors.push(error.message);
  });

  // Mobile screenshot
  console.log('Capturing mobile screenshot...');
  const mobilePage = await context.newPage();
  await mobilePage.setViewportSize({ width: 375, height: 667 });
  await mobilePage.goto('https://arkify.app', { waitUntil: 'networkidle' });

  await mobilePage.waitForTimeout(3000);

  await mobilePage.screenshot({
    path: 'output/qa-mobile.png',
    fullPage: true
  });
  console.log('Mobile screenshot saved to output/qa-mobile.png');

  // Collect diagnostic data
  const diagnostics = await desktopPage.evaluate(() => {
    const images = Array.from(document.querySelectorAll('img'));
    const svgs = Array.from(document.querySelectorAll('svg'));
    const canvases = Array.from(document.querySelectorAll('canvas'));

    return {
      imageCount: images.length,
      imagesLoaded: images.filter(img => img.complete && img.naturalHeight > 0).length,
      svgCount: svgs.length,
      canvasCount: canvases.length,
      bodyHeight: document.body.scrollHeight,
      title: document.title,
      hasBarChart: document.querySelector('[class*="bar"]') !== null,
      hasCircular: document.querySelector('circle') !== null || document.querySelector('[class*="circular"]') !== null,
      hasNetwork: document.querySelector('[class*="network"]') !== null || document.querySelector('[class*="diagram"]') !== null
    };
  });

  console.log('\n=== DIAGNOSTICS ===');
  console.log(JSON.stringify(diagnostics, null, 2));

  if (pageErrors.length > 0) {
    console.log('\n=== PAGE ERRORS ===');
    pageErrors.forEach(err => console.log(err));
  }

  if (consoleLogs.length > 0) {
    console.log('\n=== CONSOLE LOGS ===');
    consoleLogs.forEach(log => console.log(`[${log.type}] ${log.text}`));
  }

  await browser.close();
  console.log('\nQA check complete!');
})();
