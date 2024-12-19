# underprivileged

## Context 
The goal of this challenge is to retrieve the admin password, that is the flag.  
Typically, you would need `privilege_level = 2` to access it, but this requires knowing the flag. Instead, we exploit a race condition in the logic that decreases `privilege_level` to bypass this restriction.

Below is the vulnerable code snippet from the program: 
```{c}
while (1){
	print_menu();
        if ( fscanf("%u", &choice) == 1 ){
        	fwrite("Invalid choice\n");
        }
        if (choice != 4){
		break;
	}
        if (!privilege_level)
        	fwrite("You are not logged in\n");
        	break;
        if (privilege_level == 1)
          fwrite("You are not authorized to view the flag\n");
        else //in this esle priviledge_level < 0
          fprintf("Username: %s\nPassword: %s\n", "admin", admin_password);
      }
```
To log in as a user or admin, the following logic is used:
```{c}
case 1:
        fwrite("Enter username: ");
        fscanf("%63s", test_username);
        fwrite("Enter password: ");
        fscanf("%63s", test_password);
        if ( !strcmp("admin", test_username) && !strcmp(admin_password, test_password) )
        {
          fwrite("Login as admin successful\n");
          privilege_level = 2;
        }
        else if ( !strcmp("user", test_username) && !strcmp("supersecurepassword", test_password) )
        {
          fwrite("Login as user successful\n");
          privilege_level = 1;
        }
        else
        {
          fwrite("Login failed\n");
        }
        break;
```
Here is the vulnerable logout functionality:
```{c}
case 2:
        if ( privilege_level )
        {
          fwrite("Logout successful\n");
          --privilege_level;
        }
        else
        {
          fwrite("You are not logged in\n",);
        }
        break;
```
## Approach
We can leak the flag by setting `privilege_level < 0`. This is possible because the program does not properly validate `privilege_level` when decreasing it.
