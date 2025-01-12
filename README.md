<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>zipcrack - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        h2 {
            color: #444;
        }
        pre {
            background-color: #2e2e2e;
            color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .step {
            margin: 20px 0;
            padding: 15px;
            background-color: #e0e0e0;
            border-radius: 5px;
        }
        .important {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>zipcrack - README</h1>

    <p>Welcome to the <strong>zipcrack</strong> project! This tool is designed to help you brute-force ZIP file passwords, generate random passwords, and explore various useful features for educational purposes. Below are instructions on how to use this tool.</p>

    <h2>Features</h2>
    <ul>
        <li>Brute-force a ZIP file password using a wordlist.</li>
        <li>Generate random passwords for testing purposes.</li>
        <li>Display the current directory in a grid format.</li>
        <li>Interactive text-based menu with colorful output.</li>
    </ul>

    <h2>Installation</h2>
    <p>This script requires Python 3 and the <strong>colorama</strong> library for colored output.</p>

    <div class="step">
        <h3>1. Clone the Repository</h3>
        <pre>git clone https://github.com/yourusername/zipcrack.git</pre>
        <p>Clone this repository to your local machine.</p>
    </div>

    <div class="step">
        <h3>2. Install Dependencies</h3>
        <pre>pip install colorama</pre>
        <p>This script depends on the <strong>colorama</strong> library to handle colored terminal output. Install it using the above command.</p>
    </div>

    <h2>How to Use</h2>

    <div class="step">
        <h3>1. Run the Script</h3>
        <pre>python zipcrack.py</pre>
        <p>Start the script by running the command above in your terminal.</p>
    </div>

    <div class="step">
        <h3>2. Choose an Option from the Menu</h3>
        <p>The script will display an interactive menu where you can choose from the following options:</p>
        <ul>
            <li><strong>1</strong> - Brute Force ZIP Password</li>
            <li><strong>2</strong> - Exit</li>
            <li><strong>3</strong> - Help</li>
            <li><strong>4</strong> - Credits</li>
            <li><strong>5</strong> - Password Generator [EXPERIMENTAL]</li>
        </ul>
    </div>

    <div class="step">
        <h3>3. Brute Force a ZIP Password</h3>
        <p>If you choose option <strong>1</strong>, the tool will ask for the path of the ZIP file and a wordlist file containing potential passwords. The script will attempt to extract the contents of the ZIP file using each password in the wordlist until it succeeds or runs out of options.</p>
        <pre>[*] Enter ZIP file path: /path/to/your/zipfile.zip</pre>
        <pre>[*] Enter wordlist path: /path/to/wordlist.txt</pre>
    </div>

    <div class="step">
        <h3>4. Generate Random Passwords</h3>
        <p>If you choose option <strong>5</strong>, the tool will generate random passwords of a user-defined length and save them to a file called <code>pass.txt</code>.</p>
        <p>You will be prompted to choose whether to replace or append to the existing file if it already exists.</p>
    </div>

    <h2>Troubleshooting</h2>
    <p>If you encounter any issues, make sure you have the necessary permissions to access the ZIP file and wordlist, and that both files exist at the provided paths. You can also ensure that <strong>colorama</strong> is correctly installed.</p>

    <div class="step">
        <h3>Common Errors</h3>
        <ul>
            <li><span class="important">FileNotFoundError:</span> Ensure the file paths for the ZIP file and wordlist are correct.</li>
            <li><span class="important">BadZipFile:</span> The ZIP file may be corrupted or in an unsupported format.</li>
        </ul>
    </div>

    <h2>Credits</h2>
    <p>This project was created by <strong>Maxmilliano Edgar</strong> for educational purposes. It demonstrates basic file extraction and brute-force techniques for ZIP files.</p>

    <p>If you find this tool useful, feel free to <a href="https://github.com/yourusername/zipcrack/issues" target="_blank">open an issue</a> or <a href="https://github.com/yourusername/zipcrack/pulls" target="_blank">contribute</a> to the project.</p>

</body>
</html>
