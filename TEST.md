## Testing 


### First Time User Goals

- As a first time user, I would like to be able to access the Home page and navigate the contents of this website.
- As the site loads, the users will see the Home page and navigation bar at the top of the page which contains menu items. 
- The menu items in the navigation bar allow users to access the page(s) of their choice.
- All the menu items to access the pages tested and all those took the users to the correct pages.
- As the first time user, I will able to search and look up older post which were made by other users. There descrition.
- If the searched name is there then the result will show otherwise a black area will be there. If the result is present then on clicking the activator three dots I can slide the card up and see the description and the other information. 
-  I would like to be able to register and create my own account on the website.
- In the navigation bar at the top of the page, click on the Register and it will redirect the users to the registration page.
- The users will be able create their own desired username and add their desired password, then click the register button.
- Once registration is completed, a flash message will show to confirm the registration is successful
 I would like to login and be able to add, edit and remove my own jobs.
- Once the users have successfully registered, they will be able to login by clicking the Login menu in the navigation bar.
- The login page will be displayed with username and password fields to be filled in, then the users need to click on the login button.
- Once the login is successful, the users will be redirected to the Profile page where they would be able to display there name. 
- Once the user is logged in they will see more menu options like Profile, Add Services and Logout. 
- On clicking on the Add Services the first time user will be able to post there first requirement by filling out a simple form. 
- The first time user will fill out the required fields on the add services form which includes, a drop down for the categories which they can select one, enter you name, Job description, contact, email and date the job needs to be done. Then by submitting the form a flash message will appear stating that your service has been added successfully. 
- The user can view the posted service at the bottom of the home page which will display there name, the date and the category for which they want the service. On clicking on the activator the three dots they will be able to see all the other details regarding there post. 
- At the end the user can logout and continue to see there service on the home page.

### Frequent User Goals

- As a frequent user, I would like to be able to search for any specific services on the website.
- In the Home page, there is a search function which allows users to find their desired services available by typing in the name of the services.
- If the service is available, the search result will display the service and if the service is unavailable, the search result will be blank.
- Once the search result is displaying the available service(s), users will be able to display the details of service(s) by clicking the service name, the slide card will move up and will the description.
- If at this time returning user feels that the service they posted need to be changed then there is an edit button which will direct them to the add service page. There old form will be present with the filled out fields. The user can edit any field they desire to edit and click on 'Save' button or they can click on the cancel button to if they change there mind. 
- If they edit the changes will be updated and they will be able to see the changes on the new post at the bottom of the home page. 
- The returning user can add more services by adding new services by clicking on the add services and following the same steps which were done by a new user.
- They will see the new posted service on the home page along with the old service which was added previously.
- The user can log out after making the changes.

### Return User Goals

- As a frequent user, I would like to be able to search for any specific services on the website.
- In the Home page, there is a search function which allows users to find their desired services available by typing in the name of the services.
- If the service is available, the search result will display the service and if the service is unavailable, the search result will be blank.
- Once the search result is displaying the available service(s), users will be able to display the details of service(s) by clicking the service name, the slide card will move up and will the description.
- If at this time returning user feels that the service they posted need to be changed then there is an edit button which will direct them to the add service page. There old form will be present with the filled out fields. The user can edit any field they desire to edit and click on 'Save' button or they can click on the cancel button to if they change there mind. 
- If they edit the changes will be updated and they will be able to see the changes on the new post at the bottom of the home page. 
- The returning user can add more services by adding new services by clicking on the add services and following the same steps which were done by a new user.
- They will see the new posted service on the home page along with the old service which was added previously.
- The user can log out after making the changes.

## Responsiveness
This project was required to be totally responsive, and mobile friendly therefore I decided to use Materialize as my main framework for it's cut down components that result in a clean, uncluttered view and minimize to add custom styles. Testing was done using dev-tool during build process, and also a final test of the entire website was done using Android phone to check its responsives.
- Page was responsive overall and no major issue noticed however here was slightly issue with excess whitespace above and below footer while viewing on Android phone and specially search bar and the rest and search button would position themselves into coloums

### Navbar 
- Navbar displays 3 links before logging in which are home, login and registration. 
- Navbar working fine on the medium to small devices and the side nav is displayed at 975px. It slides in from the right side display the same number of nav links before logging in.
- After logging in the nav links there are 4 links appearing including the home which is common to all the users. 
- Sliding right to left working smoothly across all the devices.

### Search field
- The search bar appears below the content of text. The search will look for words which are in the category name and the job descriprtion. If the words are present then the card with that search will appear in the lower section of the services field. 
- The search is by entering the name on a line and is a required field if searched without any name or word the field will appear in red line. 
- Once the word is entered simply click on the search button.
- The result will appear on the lower area of the services field. 
- For next time I would like to add the search to display directly under the search line since this is not giving a visual feedback to the user if any action has been there.
- Along with the search button there is a reset button which will clear the text area and will redirect you to the home page.
- On the mobile view the reset and search buttons collaps.

### Services
- There is a services field under the main image. This field post all the services which were posted by the signed up users for there jobs.
- There are extented cards which has the display of the service name, date and the user who created by on it.
- On the right side of the card there is an activation button which is denoted by three vertical dots. 
- On clicking them another card will slide up and there will be more details about your services.
- There is a delete and edit button which only appears to the user who created the service once logged in.

### Registration 
- Registration a simple form which contains an user name and password to register with proper validations. The password hash is used for added security.
- Once you fill out the user name which contains min 5 to max 15 characters and numbers. If not filled correctly then the text line will appear red because it is a required field.
- The password is case sensitive and min 5 to max 15 characters with numbers and special characters. If it doesnt meet the requirements then the text line will appear red.
- Once entering all the requirement fields just click on the registration buttom. And a flash message will appear stating you have successfully been register.
- Under the register button there is link saying if you are already a signed up then you can directly login here.

### Login
- Login is the same like the registration form which has two required fields. You need to enter the same username and password to login. 
- If the username and/or password are incorrect there will be a flash message appearing on the top of the page. Saying Username and/or Password is incorrect.
- Once you enter the correct username and password click on the login button which will direct you to the profile page.
- Under the login button there is a link which says New to the site please Register here.

### Profile
- Once you login you will be redirected to the profile page or you can just simply click on the profile link in the navbar. 
- The profile page only is displaying users name.
- I would like to add more details with this page regarding the categories entered where the user can directly delete and edit there posted services. 

### Add Services
- Now if you need to add new services simply click on the add services link in the navbar. Which will take you to the Add Services page.
- This a form that is a required field. 
- It begans with a drop down that displays all the catagories which this company takes care of.
- It needed a special validation using JS which was taken from the CI learning tutorials.
- After that there is a Enter name section which is a required field.
- There is a Job Description where the user can enter detailed text on what services they need around there house. 
- There is next field which is contact number where the company can contact the person to get better information from the user. 
- Then next field is email and the user can enter it and the company can email the user if needed.
- There is date picker which the user can pick an exact date for which the service can be done. The date can be clear by clicking on the clear or selected by clicking on the select button.
- Once all the required fields have been entered with there respective validation then the user can click on the Add Task.
- By doing so your added service will be posted on the home page under the services field.
- You can see you service which will be posted all the way in the bottom of the home page with your selected category name, your date you selected and the your name. So you can see it was created by you.
- Once you find your post you can click on the activator button which is on the right side of the card with an icon of three vertical dots. 
- By doing that another card will slide over from bottom with more fields that you entered. 
- There is a close icon on the top right to close that card and return to the previous card. 
- On the description card there are two buttons on the bottom which can only be appears once the user is in session. 

### edit Services
- Incase the users service needs to be edited just click on the edit and it will direct you to the add services page which will show your entered details. The user can edit make changes just need to click on save button to see the updated service which will be posted back on the bottom on the home page.
- If you want to cancel any changes made just click on the cancel button and there will be no changes made to your old post. 

### Delete 
- Now on the services field in the card where the description is there is delete button which will completely delete your posted services.

### Logout
- Once your done with all this you can simply logout but can see your posted service but again you cannot edit or delete it because your logged out of the session. 

## Code Validation

### Python code
- All python codes were checked by using PEP8 online checker - All codes were PEP8 compliant and no issue

### HTML codes
- HTML codes were tested using [W3C Markup Validation](https://validator.w3.org/#validate_by_input) 
 - Error jinja shown accross all the pages which is not resolved yet, this is due jinja for loop in the nav links, the block content and if statement generated while loop is running, 

### Javascript codes
- Codes were checked using [JSHINT](https://jshint.com/) - All codes passed

### CSS codes
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) used for CSS code validation - All codes passed without any error.
