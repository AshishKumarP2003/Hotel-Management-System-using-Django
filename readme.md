# Hotel Management System

## Overview

The Hotel Management System is a comprehensive solution designed to streamline hotel operations, manage rooms and guests, and facilitate reservations. This system features two main roles: Super-Admin and Admin.

- **Super-Admin**:

  - Can add hotels to the system.
  - Can create Admin accounts for each hotel.
- **Admin**:

  - Can log in with credentials provided by the Super-Admin.
  - Can manage the hotel's menu, guests, and rooms.
  - Has access to a booking panel to reserve rooms for guests.

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

1. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

1. **Activate the Virtual Environment**
  - On Windows
      ```bash
      python -m venv venv
      ```