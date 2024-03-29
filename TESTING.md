# TESTING

---

## Manual Testing

- Hover action:

When the User hovers over buttons and links the colors changes so the User can see that it is active.

 ![Title](media/images/pp4_title_unhighlighted.png)

 ![Title](media/images/pp4_title_highlighted.png)


 ![Sign Up Unhighlighted](media/images/pp4_signup_button_unhighlighted.png)

 ![Sign Up Highlighted](media/images/pp4_signup_button_highlighted.png)


 ![Sign Out Unhighlighted](media/images/pp4_signout_button_unhighlighted.png)

 ![Sign Out Highlighted](media/images/pp4_signout_button_highlighted.png)


 ![Sign Link Unhighlighted](media/images/pp4_sign_in_link_unhighlighted.png)

 ![Sign Link Highlighted](media/images/pp4_sign_in_link_highlighted.png)
 

---

- Messages:

Messages are shown to the User when an action is either successful or blocked.

 ![Account Activation](media/images/pp4_account_success_validation.png)


 ![Reservation Creation](media/images/pp4_reservation_validation.png)


 ![Updated Reservation](media/images/pp4_reservation_updated_validation.png)


 ![Delete Reservation](media/images/pp4_reservation_deleted_validation.png)


 ![Wrong Login Details](media/images/pp4_incorrect_login_credentials_validation.png)


 ![Wrong Date Selection](media/images/pp4_wrong_date_validation.png)


 ![Sign Out](media/images/pp4_signout_validation.png)

---

- Reservation Selectors:

These are for when the User is creating a reservation they are offered muliple options to choose from.

 ![Date Picker](media/images/pp4_date_picker_reservation_form.png)


 ![Time Picker](media/images/pp4_time_picker_reservation_form.png)


 ![Party Size Picker](media/images/pp4_party_size_picker_reservation_form.png)

---

- Reverted to Login page:

When a User tries to go through the URL then they are sent to the login page.

![Typed Access](media/images/pp4_typed_access.png)

![Typed Access Validation](media/images/pp4_typed_access_validation.png)

---


## Site Responsiveness

---

## Code Validation

### HTML
Html Code - [Errors](media/images/pp4_html_validation.png)

### Python

Admin.py - [Errors](media/images/pp4_css_admin.py_validation.png)

Forms.py - [Errors](media/images/pp4_css_forms.py_validation.png)

Apps.py - [Errors](media/images/pp4_css_apps.py_validation.png)

Models.py - [Errors](media/images/pp4_css_models.py_validation.png)

Views.py - [Errors](media/images/pp4_css_views.py_validation.png)

Urls.py - [Errors](media/images/pp4_css_urls.py_validation.png)

### CSS

Style.css - [Errors](media/images/pp4_css_validation.png)

### Lighthouse Validation

Lighthouse - [Valdation](media/images/pp4_lighthouse_validation.png)

---

## Testing User Stories

 **The images for the User Stories can be found in both the Features section of the README.md and above in the Manual Testing.**

---

- Menu:

The menu was made to be vibrant and noticable by the users and was presented with many options to choose.

---

- Site Navigation:

The nav bar was created and offered up all the options:

    - Sign in

    - Log Out

    - Account Creation

    - Ability to Book

    - See your Reservations

 When each button is clicked it takes the user to the appropriate page.

 ---

- Account Sign-Up:

The account page offers users fields to place their Username, Email and both Password and Password Verification. Once completed it passes the Users to the page with the ability to Book a reservation, View Details and Sign Out.

---

- Making A Reservation:

Clicking the Book button takes the User to the Reservation for, which offers users fields for the Name, Date, Time and Party Size. Once completed it will go through to the page to view the reservation and its details.

---

- Update Reservations:

On the reservation details it shows an green 'Update' button, when pressed takes the user back to the creation page and allows them to create a new reservation and once completed deletes the old reservation and places the new one in its place.

---

- Delete Reservations:

The red 'Delete' button is placed next to the 'Update' and when clicked it deletes the reservation altogether.

---

- Confirmation Message:

After every User interaction an message is displayed on the success of the action (as can be seen in the Manual Testing section)

---

- Only Users Reservations Show Up:

After making the reservation it is the only one shown to the logged in User.

---

- Dropdown Menu of Users Names Hidden From The Reservation Form:

When creating the reservation the form only asks the User for the Name to be on the reservation and not any of the Users 'Username' aswell to keep names protected.

---

- Stop Users From Selecting Previous Dates:

When Users select a date that isnt on the present day of access or in the future then an error appears and teels the User to correct the mistake.

---

- Sign In:

When the User clicks the 'Sign In' the are taken to a page with a form asking for their 'Username' and 'Password', there is a button the that asks to be rememeberd for Users easment and help for if/when they return again. There is also a link for forgotten passwords the User can click if they forgot the details.

---

- Sign Out:

When the User clicks on the 'Sign Out' button they are taken to a page to clarify that they want to Sign Out, once clarified they are then taken to the beginning page the sign in and create an account with a message confirming the successful action.

---

- Block Users From Accessing Site Witout Signing In:

When a User who is not a registered member or logged in tries to access functions through the URL, they are sent to the login page. 

---
