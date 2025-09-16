## Library Management System

A modern, intuitive Library Management System built with a powerful FastAPI backend and a responsive React frontend. This system provides distinct functionalities for library operators and readers, streamlining book borrowing and management.

### Key Features

*   **Role-Based Access Control:**  Separate interfaces and permissions for Operators and Readers ensure a secure and user-friendly experience for everyone.
*   **Efficient Book Management:** Operators can effortlessly add, update, and manage the library's entire collection.
*   **Seamless Borrowing Process:** The system simplifies the process of borrowing and returning books for both operators and readers.
*   **Real-Time Borrowing Status:** Readers can easily track their borrowed books and the time remaining before they are due, helping to prevent overdue fees.

### Roles and Functionalities

#### Operator
*   **Dashboard:** A comprehensive overview of the library's statistics, including the number of books, active readers, and current borrowings.
*   **Book Management:**  Full CRUD (Create, Read, Update, Delete) functionality for the library's book database.
*   **Reader Management:**  Ability to add, view, and manage reader accounts.
*   **Borrowing Management:**  Handle the borrowing and returning of books, with the ability to view the history of borrowings.

#### Reader
*   **Personal Dashboard:** A personalized view of all currently borrowed books.
*   **Borrowing Status:**  Monitor the status of each borrowed book, including the due date, to keep track of return deadlines.

### Technologies Used

*   **Backend:**
    *   **FastAPI:** A modern, high-performance web framework for building APIs with Python.
    *   **Pydantic:** For data validation and settings management.
    *   **SQLAlchemy:** As the SQL toolkit and Object Relational Mapper (ORM).
    *   **PostgreSQL:** A powerful, open-source object-relational database system.
*   **Frontend:**
    *   **React:** A JavaScript library for building user interfaces.
    *   **Axios:** A promise-based HTTP client for making requests to the backend API.

### Getting Started

To get a local copy up and running, follow these simple steps.

#### Prerequisites

*   Python 3.8+
*   Node.js and npm

#### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/library-management-system.git
    cd library-management-system
    ```

2.  **Backend Setup:**
    *   Navigate to the `backend` directory:
        ```sh
        cd backend
        ```
    *   Create a virtual environment:
        ```sh
        python -m venv venv
        ```
    *   Activate the virtual environment:
        *   On Windows:
            ```sh
            .\venv\Scripts\activate
            ```
        *   On macOS/Linux:
            ```sh
            source venv/bin/activate
            ```    *   Install the required Python packages:
        ```sh
        pip install -r requirements.txt
        ```
    *   Start the FastAPI server:
        ```sh
        uvicorn main:app --reload
        ```

3.  **Frontend Setup:**
    *   In a new terminal, navigate to the `frontend` directory:
        ```sh
        cd frontend
        ```
    *   Install the required npm packages:
        ```sh
        npm install
        ```
    *   Start the React development server:
        ```sh
        npm start
        ```

### Usage

Once both the backend and frontend servers are running, you can access the application in your web browser, typically at `http://localhost:3000`.

*   **Operators** can log in to access the management dashboard to perform administrative tasks.
*   **Readers** can log in to view their borrowed books and their respective due dates.