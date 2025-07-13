# Flask + Auth0 Authentication (Theory Overview)

This application demonstrates how to integrate **Auth0**—a secure, third-party authentication service—with a **Flask** web application. It highlights the use of **OAuth 2.0** and **OpenID Connect (OIDC)** protocols to enable secure user login, session management, and protected route access.

## Core Concepts

### 1. OAuth 2.0 & OpenID Connect (OIDC)
- **OAuth 2.0** is a protocol for authorization.
- **OIDC** is an identity layer built on top of OAuth 2.0, enabling authentication and user information retrieval.
- Auth0 uses OIDC to authenticate users and return ID tokens and user profile information.

### 2. Auth0 Integration
- Auth0 acts as an identity provider (IdP).
- The Flask app registers Auth0 as an OAuth client using the `authlib` library.
- Key configurations (like client ID, secret, and domain) are set via environment variables.

### 3. Environment Variables
The app reads sensitive values (like secret keys and Auth0 credentials) from environment variables using the `dotenv` package. This keeps secrets secure and separate from the codebase.

### 4. Session Management
- Once a user is authenticated via Auth0, their profile is stored in Flask’s session.
- The session is used to maintain authentication state between requests.

### 5. Route Protection
- Public routes (e.g., `/`) are accessible to everyone.
- Protected routes (e.g., `/dashboard`) check for a valid user session.
- If no session is found, the user is redirected to the login page.

### 6. Login Flow
1. User visits `/login`.
2. Flask redirects to Auth0's hosted login page.
3. After successful login, Auth0 redirects the user back to `/callback`.
4. The app extracts user info and stores it in the session.
5. The user is redirected to `/dashboard`.

### 7. Logout Flow
- When the user logs out via `/logout`, the session is cleared.
- The user is redirected to Auth0's logout endpoint, which then returns them to the home page.

### 8. Templates
- `index.html`: Public-facing home page.
- `dashboard.html`: Displays authenticated user information.

## Summary

This app serves as a basic but secure implementation of user authentication in a Flask application using Auth0. It demonstrates best practices in identity management, session handling, and secure route protection using modern web authentication standards.

