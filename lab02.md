
# Lab: Penetration Testing on a Web Application

In this lab, you will learn how to perform penetration testing on a web application. You are provided with a vulnerable Python/Flask web application containing common vulnerabilities. The link to the web application is [here](https://15d2-101-99-6-42.ngrok-free.app/).

This is white-box penetration testing, meaning you have access to the source code of the web application. The code is available in [this folder](https://github.com/mtuann/COMP4030-Spring24-CyberSecurity/tree/main/lab-02). You can clone the repository using the following command:

```bash
git clone https://github.com/mtuann/COMP4030-Spring24-CyberSecurity.git
```

You do not need to run the web application on your local machine. You can use the web application provided [here](https://15d2-101-99-6-42.ngrok-free.app/).

Below is the list of vulnerabilities that you will discover in this lab:

- SQL Injection (Login, Search)
- Cross-Site Scripting (XSS)
- Server-Side Request Forgery (SSRF)
- File Upload Vulnerability
- Path Traversal
- Insecure Direct Object Reference (IDOR)
- IFrame Injection

For each vulnerability, you need to provide a brief description, steps to reproduce, identify the vulnerable code, and suggest a fix if possible.

Here's the template for the SQL Injection vulnerability:

- **Vulnerability:** SQL Injection
- **Description:** SQL Injection is a code injection technique that might destroy your database. It is one of the most common web hacking techniques. SQL Injection is the placement of malicious SQL queries via web page input.
- **Steps to reproduce:**
  1. Go to the login page at [here](https://15d2-101-99-6-42.ngrok-free.app/sql-injection/login)
  2. Enter the following username `admin';---` and password: `password`
  3. Click on the `Signin` button, the website allows you to sign in as 'Admin' without the password.
- **Code:** The code that causes the vulnerability is in the `sql_injection_login_api` function in the `vulns/sql_injection/sql_injection_login.py` file. (Specify which lines, why these lines are vulnerable, what was wrong, etc.)
- **Fix:** To fix the vulnerability, you need to use ORM (Object-Relational Mapping), with a combination of input sanitizing, etc. (You can name more, if you can, provide a sample fix of the vulnerable lines).

For a better understanding of the vulnerability, you can provide a captured image (screenshot) of the web page that shows the vulnerability.

Your task is to find at least 4 vulnerabilities in the web application and provide the information as described above.

