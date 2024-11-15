# Crowbar

Crowbar is a Brute Forcer for web applications. By now, it breaks through "http://testphp.vulnweb.com/login.php", a website made for exploring vulnerabilities and practicing your pentesting skills.

1- At first, it identifies fields to navigate to a register page, so the brute force can be properly done, as the website doesn't have any database.
2- It's asked for the users' Users wordlist path, and also for the Passwords wordlist path too.
3- When the new account is created, Crowbar now starts filling the fields in a way all the possible combinations of the Users and Passwords wordlists are inputed.
4- With that being done, the brute force is completed and you have total access to the account identified.
