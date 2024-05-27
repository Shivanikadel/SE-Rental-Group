# SE-Rental-Group

(MRS) was created to address the housing needs near Clayton (SE Group Project). It is a basic housing application designed for students to find suitable accommodation. This system simplifies the process for tenants to find rental space.

## Functionalities

The application includes the following functionalities:
- Tenant Login / Logout
- Property Browsing
- Submitting Application
- Saved Property Management & Utility

## Project Structure

The project consists of the following Python files:
- `application.py`
- `boundary.py`
- `mrs.py` (Main controller class)
- `property.py`
- `tenant.py`
- `utility.py`
- `watchlist.py`

The main file to be executed is `mrs.py`, which handles the primary logic for the application.

## Installation Guide

### Prerequisites

- Python version > 3.7
- A Python IDE / Command Line Interface

This tutorial primarily illustrates how to run the application on Windows CLI.

### Steps to Install and Run the Application

1. Import the entire project folder (including the text files) to your local system.
2. Unzip and extract the folder.
3. Open CLI from the root directory containing all the files.
4. Run `mrs.py` to start the application.

## User Interface

1. **Login into MRS** using `tenant@student.monash.edu` and the password `Monash1234`.
   - Note: Currently, the system supports only this user; however, this may be updated in the future.

2. The **home screen** is displayed with the following self-explanatory options:
   1. Browse properties
   2. See wishlisted properties
   3. Logout
   4. Exit

   Choose `1` to browse properties or `2` to see previously wishlisted properties.

### Browse Properties

- This displays all available properties in the system. Users can view more details for a specific property and then choose to wishlist that property or submit an application for that property.

### See Wishlisted Properties

- This displays all the properties wishlisted by the tenant. Users can view more details for a specific property and then choose to submit an application for that property.

## Data Management

- **Registered Users and Properties:** Data for registered users and properties has been created by the development team in the files `registered_users.txt` and `properties.txt`.
- **Watchlist:** To store the watchlist of the logged-in tenant, the watchlists are saved in the file `watchlist.txt`. This ensures that even if the tenant logs out and logs back in, their watchlist persists.
- **Applications:** To keep track of applications created by the tenant, information about created applications is stored in the file `application.txt`. This ensures that a tenant can apply to a property only once.

## Running the Application on Command Line

1. Open the terminal on your operating system.
2. Navigate to the unzipped application folder using the command:
   ```sh
   cd <folder name>
3. Inside the folder, you will see a list of all files that our application uses.
4. Run the following command to start the application   
  ```sh
   python3 mrs.py
