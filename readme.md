# Hotel Management System ( Django Framework )

## Overview

The Hotel Management System is a comprehensive solution designed to streamline hotel operations, manage rooms and guests, and facilitate reservations. This system features two main roles: Super-Admin and Admin.

- **Super-Admin**:
  
  - Can add hotels to the system.
  - Can create Admin accounts for each hotel.
- **Admin**:
  
  - Can log in with credentials provided by the Super-Admin.
  - Can manage the hotel's menu, guests, and rooms.
  - Has access to a booking panel to reserve rooms for guests and check-out.

The project is hosted on [PythonAnywhere](http://raftar2003.pythonanywhere.com).

## Features

### Super-Admin

- Add new hotels to the system.
- Create and manage Admin accounts for each hotel.

### Admin

- Log in to the system with provided credentials.
- Manage hotel menu:
  - Add, update, and delete menu items.
- Manage guests:
  - Add, update, and delete guest information.
- Manage rooms:
  - Add, update, and delete room details.
- Booking panel:
  - Reserve rooms for guests.
  - View and manage current reservations.

## Installation

To run the project locally, follow these steps:

### Prerequisites

- Python 3.x installed on your local machine.
- `virtualenv` package installed.

### Steps

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/yourusername/hotel-management-system.git
   cd hotel-management-system
   ```
2. **Create a Virtual Environment**
   
   ```bash
   python -m venv venv
   ```
3. **Activate the Virtual Environment**
   
   - On Windows
     
     ```bash
     venv/Scripts/activate
     ```
   - On Mac
     
     ```bash
     source venv/bin/activate
     ```
4. **Install Required Packages**
   
   ```bash
   pip install -r requirements
   ```
5. **Run the Server**
   
   ```bash
   pip install -r requirements
   ```

## Usage

### Access the Application

- Visit [http://raftar2003.pythonanywhere.com](http://raftar2003.pythonanywhere.com) to access the hosted version of the application.

### Super-Admin Functions

1. Log in with Super-Admin credentials.
2. Add new hotels and create Admin accounts for each hotel.

### Admin Functions

1. Log in with Admin credentials provided by the Super-Admin.
2. Manage the hotel’s menu, guests, and rooms.
3. Use the booking panel to handle room reservations.
   

