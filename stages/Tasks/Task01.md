

## Task: Track Your Learning Progress Using GitHub

### Goal

In this task, you will learn the basics of Git and GitHub by:

* Copying (cloning) an existing project
* Making simple edits on your computer
* Using Git to save your progress
* Publishing your own version of the project on GitHub

You do **not** need prior Git experience.

---

### Project to Use

Progress Tracker Repository:
[https://github.com/heyad/Progress-Tracker](https://github.com/heyad/Progress-Tracker)

---

## Step-by-Step Instructions

### Step 1: Clone the Project to Your Computer

1. Open the link above in your browser.
2. Click the **Code** button and copy the repository URL.
3. Open a terminal (or Git Bash).
4. Run the following command:

   ```bash
   git clone https://github.com/heyad/Progress-Tracker.git
   ```
5. A new folder named `Progress-Tracker` will appear on your computer.
6. Move into the folder:

   ```bash
   cd Progress-Tracker
   ```

---

### Step 2: Look Around the Project

1. Open the project folder in your code editor (or file explorer).
2. Open the `README.md` file.
3. Read how the progress tracker works.
4. Find where progress is written (for example: checklists, tables, or notes).

👉 At this stage, **do not worry about understanding everything**. Just explore.

---

### Step 3: Update the Progress Tracker

1. Edit the files to show **your own progress**:

   * Add your name (if appropriate)
   * Mark items as completed
   * Add notes or dates
2. Save the file(s).

---

### Step 4: Save Your Changes with Git

1. In the terminal, check what you changed:

   ```bash
   git status
   ```
2. Add your changes:

   ```bash
   git add .
   ```
3. Save them with a message:

   ```bash
   git commit -m "Updated my learning progress"
   ```

💡 You can repeat this step whenever you make new progress.

---

### Step 5: Create Your Own GitHub Repository

1. Go to **GitHub** and log in.
2. Click **New Repository**.
3. Give it a name (for example: `my-progress-tracker`).
4. Do **not** add a README (important).
5. Create the repository.

---

### Step 6: Connect Your Project to Your GitHub Account

1. Remove the old connection:

   ```bash
   git remote remove origin
   ```
2. Copy the URL of your new GitHub repository.
3. Connect your project to it:

   ```bash
   git remote add origin <your-repository-url>
   ```
4. Upload your project:

   ```bash
   git push -u origin main
   ```

---





