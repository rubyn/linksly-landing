# Linksly Landing Page

A modern, responsive landing page for the Linksly iOS app built with Flask and vanilla JavaScript.

## Features

- **SEO Optimized** - Complete meta tags, Open Graph, and Twitter Card support
- **Responsive Design** - Mobile-first approach with tablet and desktop breakpoints
- **Modern Animations** - Smooth scrolling, fade-in effects, and interactive elements
- **Email Capture** - Modal-based newsletter signup with form validation
- **Performance Optimized** - Minimal dependencies, optimized images, and clean code

## Technology Stack

- **Backend**: Flask 2.3.3
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Inter (Google Fonts)
- **Testing**: Playwright for automated browser testing

## Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd linksly-landing
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

5. Visit `http://localhost:5001` to view the landing page.

## Testing

Run automated tests with Playwright:

```bash
python test_landing.py
```

This will:
- Test all major page elements
- Capture screenshots for desktop, tablet, and mobile views
- Test interactive elements (modals, forms, navigation)
- Verify responsive design

## Deployment

### Heroku

1. Install Heroku CLI
2. Create Heroku app:
```bash
heroku create your-app-name
```

3. Deploy:
```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

### Other Platforms

The app is configured to work with any platform that supports:
- Python 3.12+
- WSGI servers (Gunicorn included)
- Static file serving

## File Structure

```
linksly-landing/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── runtime.txt           # Python version specification
├── test_landing.py       # Playwright test suite
├── templates/
│   └── index.html        # Main landing page template
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── main.js       # Interactive functionality
│   └── images/
│       ├── logo.svg      # Linksly logo
│       └── app-screenshot.svg  # App mockup
└── venv/                 # Virtual environment (ignored)
```

## Customization

### Content Updates

Edit `app.py` to update:
- Meta tags (title, description, keywords)
- App Store URLs
- Domain configuration

### Design Changes

- **Colors**: Update CSS custom properties in `:root`
- **Typography**: Modify font imports and CSS font-family declarations
- **Layout**: Adjust grid systems and spacing in `style.css`

### Features

- **Email Collection**: Emails are logged to `subscribers.txt` - integrate with your preferred email service
- **Analytics**: Add Google Analytics or other tracking scripts to the HTML template
- **A/B Testing**: Create multiple templates or use feature flags

## SEO Checklist

✅ Meta title and description
✅ Open Graph tags
✅ Twitter Card tags
✅ Canonical URLs
✅ Semantic HTML structure
✅ Alt text for images
✅ Mobile-friendly design
✅ Fast loading times
✅ Clean URLs

## Performance

The landing page is optimized for performance:
- Minimal JavaScript (no frameworks)
- Optimized CSS with modern features
- SVG graphics for scalability
- Efficient font loading
- Responsive images

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

MIT License - see LICENSE file for details.