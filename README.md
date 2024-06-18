# Urine Strip Analyzer

The Urine Strip Analyzer is a web application that allows users to upload images of their urine strips and processes these images to detect and analyze the colors on the strips. This project uses Django for the backend and OpenCV for image processing.

## Features

- Upload images of urine strips.
- Analyze the colors in the images.
- Return RGB values of detected colors.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **OpenCV**: A library of programming functions mainly aimed at real-time computer vision.
- **JavaScript**: Used for frontend interaction.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- OpenCV
- Node.js and npm (for frontend dependencies)

### Installation

1. **Clone the Repository**

   Clone the repository from GitHub:

   ```bash
   git clone https://github.com/yourusername/urine-strip-analyzer.git
   cd urine-strip-analyzer

   ```

2. **Set Up Virtual Environment**

Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

Install the required Python dependencies:

bash
Copy code
pip install -r requirements.txt
For frontend dependencies, navigate to the frontend directory and install:

bash
Copy code
cd frontend
npm install

4. **Database Migrations**

Apply database migrations:

bash
Copy code
python manage.py migrate 5. **Run the Server**

Start the Django development server:

bash
Copy code
python manage.py runserver
Navigate to http://127.0.0.1:8000/ to view the application.

6. **Upload an Image**

Use the web interface to upload an image of a urine strip. The application will process the image and return the RGB values of the detected colors.
