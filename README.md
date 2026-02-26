# Argus — Multi Modal Edge AI System for Anomaly Detection in Pharmaceutical Manufacturing

A user-friendly showcase website for the Multi Modal Edge AI System project.

**Live website:** https://noahmathew.github.io/SeniorWeb_EdgeCompute/

## GitHub Pages Deployment

### Option 1: Deploy from branch (recommended)

1. Push this repository to GitHub
2. Go to **Settings** → **Pages** in your repository
3. Under **Build and deployment** → **Source**, select **Deploy from a branch**
4. Choose the **main** (or **master**) branch and **/ (root)** folder
5. Click **Save**
6. Your site will be live at `https://noahmathew.github.io/SeniorWeb_EdgeCompute/` within a few minutes

### Option 2: Deploy from /docs folder

If you prefer to keep the site in a subfolder:

1. Move `index.html` and `.nojekyll` into a `docs` folder
2. In **Settings** → **Pages**, select **Deploy from a branch**
3. Choose **main** branch and **/docs** folder

## Replacing Placeholders

- **Videos**: Add `.mp4` files to the `videos/` folder and update the `<source src="...">` paths in `index.html`
- **Images**: Add images to the `photos/` folder and replace the `placehold.co` URLs in `index.html` with your image paths

## Project Structure

```
├── index.html      # Main website
├── .nojekyll       # Bypasses Jekyll processing
├── videos/         # Video assets
├── photos/         # Image assets
└── README.md       # This file
```
