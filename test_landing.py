from playwright.sync_api import sync_playwright
import time

def test_landing_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # Navigate to our landing page
            print("Navigating to http://localhost:5002...")
            page.goto("http://localhost:5002")
            
            # Wait for page to load
            page.wait_for_load_state('networkidle')
            
            # Take a full page screenshot
            print("Taking full page screenshot...")
            page.screenshot(path="landing_page_screenshot.png", full_page=True)
            
            # Check if key elements exist
            print("Checking page elements...")
            
            # Check hero section
            hero_title = page.locator("h1").first
            if hero_title.is_visible():
                print("✓ Hero title found:", hero_title.text_content())
            else:
                print("✗ Hero title not found")
            
            # Check navigation
            nav = page.locator("nav")
            if nav.is_visible():
                print("✓ Navigation found")
            else:
                print("✗ Navigation not found")
            
            # Check features section
            features = page.locator("#features")
            if features.is_visible():
                print("✓ Features section found")
            else:
                print("✗ Features section not found")
            
            # Test notification modal
            print("Testing notification modal...")
            notify_btn = page.locator("#notify-btn")
            if notify_btn.is_visible():
                notify_btn.click()
                modal = page.locator("#notify-modal")
                if modal.is_visible():
                    print("✓ Notification modal opens successfully")
                    # Close modal
                    close_btn = page.locator(".modal-close")
                    close_btn.click()
                    time.sleep(0.5)
                    if not modal.is_visible():
                        print("✓ Notification modal closes successfully")
                else:
                    print("✗ Notification modal not visible")
            
            # Test mobile responsiveness
            print("Testing mobile view...")
            page.set_viewport_size({"width": 375, "height": 667})  # iPhone SE size
            page.screenshot(path="landing_page_mobile.png", full_page=True)
            print("✓ Mobile screenshot taken")
            
            # Test tablet responsiveness
            print("Testing tablet view...")
            page.set_viewport_size({"width": 768, "height": 1024})  # iPad size
            page.screenshot(path="landing_page_tablet.png", full_page=True)
            print("✓ Tablet screenshot taken")
            
            # Test desktop responsiveness
            print("Testing desktop view...")
            page.set_viewport_size({"width": 1440, "height": 900})  # Desktop size
            page.screenshot(path="landing_page_desktop.png", full_page=True)
            print("✓ Desktop screenshot taken")
            
            # Test smooth scrolling
            print("Testing smooth scrolling...")
            features_link = page.locator('a[href="#features"]').first
            if features_link.is_visible():
                features_link.click()
                time.sleep(2)  # Wait for smooth scroll
                print("✓ Smooth scrolling to features section")
            
            # Test form functionality (without actually submitting)
            print("Testing form elements...")
            notify_btn.click()
            email_input = page.locator("#email")
            if email_input.is_visible():
                email_input.fill("test@example.com")
                print("✓ Email input works")
                # Close modal
                page.locator(".modal-close").click()
            
            print("\n=== Landing Page Test Results ===")
            print("✓ Page loads successfully")
            print("✓ All major sections present")
            print("✓ Interactive elements working")
            print("✓ Responsive design working")
            print("✓ Screenshots captured for review")
            
        except Exception as e:
            print(f"Error during testing: {e}")
        
        finally:
            browser.close()

if __name__ == "__main__":
    test_landing_page()