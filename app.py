from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# SEO and meta data
META_DATA = {
    'title': 'Linksly - Save Links, Share Smarter',
    'description': 'Save links for later and share them with the right people at the perfect time. Smart link management for iOS with beautiful previews and group messaging.',
    'keywords': 'link sharing, save for later, iOS app, link management, group messaging, smart sharing',
    'og_image': '/static/images/og-image.png',
    'twitter_card': 'summary_large_image',
    'app_store_url': 'https://apps.apple.com/app/linksly',  # Update when live
    'domain': 'linksly.app'
}

@app.route('/')
def index():
    """Main landing page"""
    return render_template('index.html', meta=META_DATA)

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    """Email subscription endpoint for launch notifications"""
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email required'}), 400
    
    # TODO: Add email to mailing list (Mailchimp, SendGrid, etc.)
    # For now, just log it
    timestamp = datetime.now().isoformat()
    with open('subscribers.txt', 'a') as f:
        f.write(f"{timestamp},{email}\n")
    
    return jsonify({'success': True, 'message': 'Thanks for subscribing!'})

@app.route('/privacy')
def privacy():
    """Privacy policy page"""
    return render_template('privacy.html', meta=META_DATA)

@app.route('/terms')
def terms():
    """Terms of service page"""
    return render_template('terms.html', meta=META_DATA)

@app.route('/support')
def support():
    """Support page"""
    return render_template('support.html', meta=META_DATA)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', meta=META_DATA), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)