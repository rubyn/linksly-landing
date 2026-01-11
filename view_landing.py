from playwright.sync_api import sync_playwright
import time

def view_landing_page():
    with sync_playwright() as p:
        # Launch browser in visible mode (not headless)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            print("Opening landing page at http://localhost:5002...")
            page.goto("http://localhost:5002")
            
            # Wait for page to load
            page.wait_for_load_state('networkidle')
            
            print("Landing page is now open! You can interact with it.")
            print("The browser window will stay open for 60 seconds...")
            print("Press Ctrl+C to close earlier if needed.")
            
            # Keep the browser open for viewing
            time.sleep(60)
            
        except KeyboardInterrupt:
            print("\nClosing browser...")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    view_landing_page()