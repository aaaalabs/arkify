const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  try {
    const page = await browser.newPage();
    const outputDir = path.join(__dirname, 'output');
    
    // Desktop full page screenshot
    console.log('Capturing desktop full page...');
    await page.setViewport({ width: 1400, height: 1080 });
    await page.goto('https://arkify.app', { waitUntil: 'networkidle2', timeout: 60000 });
    await new Promise(r => setTimeout(r, 3000)); // Wait for animations
    await page.screenshot({
      path: path.join(outputDir, 'landing-full-desktop.png'),
      fullPage: true
    });
    console.log('✓ Desktop full page saved');

    // Desktop hero section
    console.log('Capturing hero section...');
    await page.setViewport({ width: 1400, height: 900 });
    await page.goto('https://arkify.app', { waitUntil: 'networkidle2' });
    await new Promise(r => setTimeout(r, 2000));
    await page.screenshot({
      path: path.join(outputDir, 'landing-hero.png')
    });
    console.log('✓ Hero section saved');

    // Mobile full page screenshot
    console.log('Capturing mobile full page...');
    await page.setViewport({ width: 375, height: 667 });
    await page.goto('https://arkify.app', { waitUntil: 'networkidle2' });
    await new Promise(r => setTimeout(r, 3000));
    await page.screenshot({
      path: path.join(outputDir, 'landing-mobile.png'),
      fullPage: true
    });
    console.log('✓ Mobile full page saved');

    // Capture specific sections by scrolling
    await page.setViewport({ width: 1400, height: 1080 });
    await page.goto('https://arkify.app', { waitUntil: 'networkidle2' });
    await new Promise(r => setTimeout(r, 2000));

    // Decision tree section (scroll ~1000px)
    console.log('Capturing decision tree section...');
    await page.evaluate(() => window.scrollTo(0, 1000));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({
      path: path.join(outputDir, 'landing-decision-tree.png')
    });
    console.log('✓ Decision tree section saved');

    // Failure gallery section (scroll ~2000px)
    console.log('Capturing failure gallery section...');
    await page.evaluate(() => window.scrollTo(0, 2000));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({
      path: path.join(outputDir, 'landing-failure-gallery.png')
    });
    console.log('✓ Failure gallery section saved');

    // Agent spectrum section (scroll ~3000px)
    console.log('Capturing agent spectrum section...');
    await page.evaluate(() => window.scrollTo(0, 3000));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({
      path: path.join(outputDir, 'landing-agent-spectrum.png')
    });
    console.log('✓ Agent spectrum section saved');

    // Meta counter section (scroll to bottom)
    console.log('Capturing meta counter section...');
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({
      path: path.join(outputDir, 'landing-meta-counter.png')
    });
    console.log('✓ Meta counter section saved');
    
    console.log('\n✅ All screenshots captured successfully!');
    
  } catch (error) {
    console.error('Error capturing screenshots:', error);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
