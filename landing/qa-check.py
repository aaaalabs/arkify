#!/usr/bin/env python3
import json
from playwright.sync_api import sync_playwright
import time

def run_qa_check():
    print('Starting QA check...')

    with sync_playwright() as p:
        browser = p.chromium.launch()

        # Desktop check
        print('Capturing desktop screenshot (1920x1080)...')
        desktop_page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        console_logs = []
        page_errors = []

        desktop_page.on('console', lambda msg: console_logs.append({
            'type': msg.type,
            'text': msg.text
        }))

        desktop_page.on('pageerror', lambda error: page_errors.append(str(error)))

        desktop_page.goto('https://arkify.app', wait_until='networkidle')
        time.sleep(3)  # Wait for animations

        desktop_page.screenshot(path='output/qa-desktop.png', full_page=True)
        print('✓ Desktop screenshot saved')

        # Collect diagnostics
        diagnostics = desktop_page.evaluate('''() => {
            const images = Array.from(document.querySelectorAll('img'));
            const svgs = Array.from(document.querySelectorAll('svg'));
            const canvases = Array.from(document.querySelectorAll('canvas'));

            return {
                title: document.title,
                bodyHeight: document.body.scrollHeight,
                imageCount: images.length,
                imagesLoaded: images.filter(img => img.complete && img.naturalHeight > 0).length,
                svgCount: svgs.length,
                canvasCount: canvases.length,
                hasBarChart: !!document.querySelector('[class*="bar"]'),
                hasCircular: !!document.querySelector('circle') || !!document.querySelector('[class*="circular"]'),
                hasDecisionTree: !!document.querySelector('[class*="decision"]') || !!document.querySelector('[class*="tree"]'),
                hasNetwork: !!document.querySelector('[class*="network"]') || !!document.querySelector('[class*="diagram"]'),
                hasLineGraph: !!document.querySelector('[class*="line"]') || !!document.querySelector('[class*="graph"]'),
                fontFamilies: Array.from(new Set(
                    Array.from(document.querySelectorAll('*'))
                        .map(el => window.getComputedStyle(el).fontFamily)
                )).slice(0, 10)
            };
        }''')

        # Mobile check
        print('Capturing mobile screenshot (375x667)...')
        mobile_page = browser.new_page(viewport={'width': 375, 'height': 667})
        mobile_page.goto('https://arkify.app', wait_until='networkidle')
        time.sleep(3)

        mobile_page.screenshot(path='output/qa-mobile.png', full_page=True)
        print('✓ Mobile screenshot saved')

        # Network requests check
        network_requests = []
        desktop_page.on('response', lambda response: network_requests.append({
            'url': response.url,
            'status': response.status
        }))

        desktop_page.reload()

        browser.close()

        # Generate report
        print('\n' + '='*60)
        print('QA CHECK REPORT')
        print('='*60)

        print('\n📊 DIAGNOSTICS')
        print(json.dumps(diagnostics, indent=2))

        if page_errors:
            print('\n❌ PAGE ERRORS')
            for error in page_errors:
                print(f'  - {error}')
        else:
            print('\n✅ No page errors detected')

        if console_logs:
            print('\n📝 CONSOLE LOGS')
            for log in console_logs[:20]:  # First 20 logs
                print(f'  [{log["type"]}] {log["text"]}')

        failed_requests = [r for r in network_requests if r['status'] >= 400]
        if failed_requests:
            print('\n🌐 FAILED NETWORK REQUESTS')
            for req in failed_requests:
                print(f'  [{req["status"]}] {req["url"]}')

        print('\n' + '='*60)
        print('Screenshots saved to:')
        print('  - output/qa-desktop.png')
        print('  - output/qa-mobile.png')
        print('='*60)

if __name__ == '__main__':
    run_qa_check()
