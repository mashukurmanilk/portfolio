# Portfolio Deployment & Hosting Guide

Your portfolio has been crafted to be completely **zero-build and self-contained**. You can host it in less than 2 minutes using any of the free hosting platforms below to get your live link for the **EJP-14** submission.

---

## Option 1: GitHub Pages (Recommended & Free)
1. Initialize git (if not already done) in this folder:
   ```bash
   git init
   git add .
   git commit -m "feat: initial portfolio release with Sun & Maroon palette"
   ```
2. Create a new repository on your GitHub account (`https://github.com/mashukurmanilk/portfolio`).
3. Push your repository:
   ```bash
   git remote add origin https://github.com/mashukurmanilk/portfolio.git
   git branch -M main
   git push -u origin main
   ```
4. On GitHub, go to **Settings** → **Pages** → under **Build and deployment / Branch**, select `main` and `/ (root)` → Click **Save**.
5. Your live link will be: `https://mashukurmanilk.github.io/portfolio/`

---

## Option 2: Netlify (Instant Drag & Drop)
1. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop the `New folder` directory containing `index.html`, `style.css`, `script.js`, `background.jpg`, and the `assets/` folder directly onto the drop zone.
3. Your portfolio is immediately live with an instant URL (e.g., `https://mashukur-manik-portfolio.netlify.app`).

---

## Option 3: Vercel (Zero-Config CLI)
1. Open PowerShell or terminal in this folder.
2. Run:
   ```bash
   npx vercel
   ```
3. Follow the quick prompts (accept defaults).
4. Vercel will output a live URL (e.g., `https://portfolio-mashukurmanilk.vercel.app`).

---

## Option 4: Surge.sh (One-Line Terminal Deploy)
1. Run in PowerShell:
   ```bash
   npx surge
   ```
2. Specify the current directory `.` and choose your custom domain name (e.g., `mashukur-manik.surge.sh`).
