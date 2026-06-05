# GITHUB SETUP & GIT COMMANDS GUIDE

---

## 📝 QUICK GIT REFERENCE

### Command 1: Initialize Git Repository
```bash
cd ecommerce-analytics
git init
```
Creates a `.git` folder (hidden). This makes your folder a git repository.

---

### Command 2: Add All Files to Git
```bash
git add .
```
Stages all files for commit. The `.` means "all files in this folder."

---

### Command 3: Commit Your Changes
```bash
git commit -m "Initial commit: e-commerce analytics portfolio"
```
Saves your files with a message explaining what you did.

**Message examples:**
- `"Add Python analysis script"`
- `"Create Power BI dashboard"`
- `"Add SQL queries and README"`

---

### Command 4: Connect to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/ecommerce-analytics.git
```
Links your local folder to your GitHub repository.

Replace `YOUR_USERNAME` with your actual GitHub username!

---

### Command 5: Rename Main Branch (Optional)
```bash
git branch -M main
```
Ensures your main branch is named `main` (GitHub default).

---

### Command 6: Push to GitHub
```bash
git push -u origin main
```
Uploads all files to GitHub.

---

## 🔧 STEP-BY-STEP GITHUB SETUP

### Step 1: Create GitHub Account (if you don't have one)
1. Go to `github.com`
2. Click "Sign Up"
3. Enter email, password, username
4. Verify email

### Step 2: Create New Repository on GitHub
1. Login to GitHub
2. Click **+** icon → **New repository**
3. Fill in:
   - **Repository name:** `ecommerce-analytics`
   - **Description:** "E-commerce sales and customer analytics dashboard using SQL, Python, and Power BI"
   - **Public** (better for portfolio)
   - Check: "Add a README file" ✓
   - Check: "Add .gitignore" → Python ✓
4. Click **Create repository**

### Step 3: Copy Commands from GitHub
After creating repo, GitHub shows you commands. Copy the commands under:
**"…or push an existing repository from the command line"**

They look like:
```bash
git remote add origin https://github.com/yourusername/ecommerce-analytics.git
git branch -M main
git push -u origin main
```

---

## 🎯 FULL WORKFLOW (Copy-Paste Ready)

Open VS Code terminal in your project folder and run:

```bash
# 1. Initialize git
git init

# 2. Add all files
git add .

# 3. First commit
git commit -m "Initial commit: e-commerce analytics portfolio project"

# 4. Connect to GitHub (COPY-PASTE from your GitHub repo page)
git remote add origin https://github.com/YOUR_USERNAME/ecommerce-analytics.git
git branch -M main
git push -u origin main
```

That's it! Your project is now on GitHub. 🎉

---

## 📤 UPDATING YOUR REPOSITORY

After your first push, any future updates use:

```bash
# 1. Add changes
git add .

# 2. Commit with message
git commit -m "Add Power BI dashboard screenshots"

# 3. Push to GitHub
git push
```

---

## 📋 FOLDER STRUCTURE FOR GITHUB

Before pushing, make sure your folder looks like this:

```
ecommerce-analytics/
├── README.md
├── POWERBI_GUIDE.md
├── PROJECT_ROADMAP.md
├── .gitignore
│
├── data/
│   ├── ecommerce_data.csv
│   ├── customer_segments.csv
│   ├── monthly_trends.csv
│   └── top_products.csv
│
├── sql/
│   └── ecommerce_queries.sql
│
├── python/
│   └── ecommerce_analysis.py
│
└── visualizations/
    ├── analytics_overview.png
    ├── dashboard_export.pdf
    └── *.png files
```

---

## ⚠️ IMPORTANT: .gitignore

Create a `.gitignore` file in your root folder to exclude large files:

**File:** `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# VS Code
.vscode/
.DS_Store

# Large files (optional - keep CSV for portfolio)
# *.csv
```

This prevents huge files from being uploaded.

---

## 🔗 GITHUB URL

After pushing, your portfolio project lives at:
```
https://github.com/YOUR_USERNAME/ecommerce-analytics
```

Share this link:
- ✓ In your resume
- ✓ In cover letters
- ✓ In LinkedIn
- ✓ With recruiters

---

## 🎓 GIT CONCEPTS EXPLAINED

### Repository (Repo)
Your project folder tracked by Git.

### Commit
A saved version of your files with a message.

### Branch
A separate version of your code (usually `main` for final work).

### Remote
A copy of your repo online (GitHub).

### Push
Upload your commits to GitHub.

### Pull
Download changes from GitHub (when working with others).

---

## 💡 BEST PRACTICES

### Commit Messages
✅ **Good:**
- "Add Python analysis script"
- "Create Power BI dashboard with 6 pages"
- "Update README with findings"

❌ **Bad:**
- "fix"
- "changes"
- "update"

### What to Commit
✅ Commit:
- Python scripts
- SQL queries
- README documentation
- Configuration files

❌ Don't commit:
- Large raw data files (>100MB)
- API keys or passwords
- Temporary files

### Commit Frequency
- Commit after completing each step
- Use meaningful messages
- Small, logical commits are better than one huge commit

---

## 🆘 COMMON ISSUES

### Issue: "fatal: not a git repository"
**Solution:**
```bash
cd ecommerce-analytics  # Make sure you're in correct folder
git init               # Initialize git
```

### Issue: "remote origin already exists"
**Solution:**
```bash
git remote remove origin
git remote add origin https://github.com/yourusername/ecommerce-analytics.git
```

### Issue: "fatal: refusing to merge unrelated histories"
**Solution:**
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Issue: "Please tell me who you are" error
**Solution:**
```bash
git config --global user.email "your.email@gmail.com"
git config --global user.name "Your Name"
```

---

## 🎬 QUICK COMMANDS REFERENCE

```bash
# Check status
git status

# See your commits
git log

# See what changed
git diff

# Undo last commit (keep files)
git reset --soft HEAD~1

# See all remotes
git remote -v

# Change remote URL
git remote set-url origin https://github.com/yourusername/new-repo.git
```

---

## 📚 GITHUB PROFILE TIPS

After pushing your project, optimize your GitHub profile:

1. **Add profile picture** (recruiter favorite)
2. **Write bio:** "Data Analyst | SQL | Python | Power BI | Analytics"
3. **Pin repositories:** Pin ecommerce-analytics to top
4. **Add README.md to profile** (creates profile description)
5. **Keep repos clean:** Only portfolio-quality projects

---

## 🔐 SECURITY NOTE

**NEVER commit:**
- API keys
- Passwords
- Database credentials
- Private information

If you accidentally committed secrets:
```bash
git rm --cached filename    # Remove from tracking
echo "filename" >> .gitignore
git commit -m "Remove sensitive file"
```

---

## ✅ VERIFICATION CHECKLIST

After pushing to GitHub, verify:

- [ ] Repository is public
- [ ] README.md displays properly
- [ ] All Python scripts are visible
- [ ] SQL file is readable
- [ ] POWERBI_GUIDE.md is visible
- [ ] Visualizations folder shows images
- [ ] No data files are missing
- [ ] GitHub URL works when shared

---

## 🎯 NEXT STEP

1. Create GitHub account (if needed)
2. Create repository named `ecommerce-analytics`
3. Run the git commands in order
4. Verify on GitHub website
5. Copy link to share! 🚀

---

**Pro Tip:** Bookmark your GitHub repo URL. You'll use it for:
- Resume
- LinkedIn
- Email signature
- Cover letters
- Portfolio website

This is your work! Make it count! 💪

---

## 📞 GITHUB HELP

- GitHub Docs: https://docs.github.com
- Git Cheat Sheet: https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf
- Interactive Git Tutorial: https://learngitbranching.js.org/
