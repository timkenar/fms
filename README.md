To set up the project, follow these steps:
•	Install Django REST Framework (pip install djangorestframework).
•	Set up a virtual environment (if not already done).
•	Install project dependencies (pip install -r requirements.txt).
•	Run the development server (python manage.py runserver).
•	Test the APIs using tools like Postman or curl.
•	Ensure proper CORS headers for frontend-backend communication.
•	Consider implementing secure authentication (e.g., JWT) for production.

APIs
To upload a file, you will fill the form using the posts url - http://127.0.0.1:8000/api/fms/posts/
To access the Users List- http://127.0.0.1:8000/api/users/ 
To access the user authentication and authorization,
Admin page- http://127.0.0.1:8000/admin/ 

Sign Up the New User

Set the request type to POST.
Register:  http://127.0.0.1:8000//api/auth/register/ 
Login: http://127.0.0.1:8000//api/auth/login/
Logout: http://127.0.0.1:8000//api/auth/logout/

Notifications
notification api: http://127.0.0.1:8000/api/notify/notifications/ 

Render Table
This api allows you to create, fetch, and filter posts made by the logged-in user, and display them in a table on the frontend: 
 http://127.0.0.1:8000/api/render/posts/ 

Test the apis with postman or curl

Ensure your frontend can communicate with your backend by setting the appropriate CORS headers.

	 For production, implement a more secure authentication method like JWT.
Test each endpoint using tools like Postman or your frontend to ensure they work as expected.

Enjoy!
More changes to come!!!