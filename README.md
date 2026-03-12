# StockFlow - Product Inventory Management System

A modern, full-stack inventory management application built with **FastAPI** (Python) and **React**. StockFlow provides a clean and intuitive interface for managing product inventory with CRUD operations, search, and sorting capabilities.

![StockFlow](https://img.shields.io/badge/StockFlow-Inventory%20Management-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![React](https://img.shields.io/badge/React-18.2+-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)

## Features

- **Beautiful UI** - Soft powder blue theme that's easy on the eyes
- **Create Products** - Add new products with ID, name, description, price, and quantity
- **Update Products** - Edit existing product details
- **Delete Products** - Remove products from inventory
- **Search** - Filter products by ID, name, or description
- **Responsive Design** - Works seamlessly on desktop and mobile devices

## Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **PostgreSQL/MySQL** - Database (configurable)
- **Python-dotenv** - Environment variable management

### Frontend
- **React** - JavaScript library for building user interfaces
- **Axios** - HTTP client for API requests
- **CSS3** - Modern styling with gradients and animations

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- PostgreSQL or MySQL database
- Git

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/anusmayaa/product-fastapi.git
cd product-fastapi
```

### 2. Backend Setup

#### Create Virtual Environment
```bash
python -m venv myenv
```

#### Activate Virtual Environment
**Windows:**
```bash
myenv\Scripts\activate
```

**Mac/Linux:**
```bash
source myenv/bin/activate
```

#### Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy python-dotenv psycopg2-binary
```

#### Configure Database
Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name
```

#### Run Backend Server
```bash
uvicorn main:app --reload
```
Backend will run on `http://localhost:8000`

### 3. Frontend Setup

#### Navigate to Frontend Directory
```bash
cd frontend
```

#### Install Dependencies
```bash
npm install
```

#### Run Frontend Server
```bash
npm start
```
Frontend will run on `http://localhost:3000`

## Project Structure

```
fastapi-project/
├── frontend/                # React frontend
│   ├── public/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Main styles
│   │   ├── TaglineSection.js
│   │   ├── TaglineSection.css
│   │   └── index.js
│   └── package.json
├── myenv/                   # Python virtual environment
├── main.py                  # FastAPI application
├── models.py                # Pydantic models
├── database.py              # Database configuration
├── database_models.py       # SQLAlchemy models
├── .env                     # Environment variables
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products/` | Get all products |
| GET | `/products/{product_id}` | Get product by ID |
| POST | `/products/` | Create new product |
| PUT | `/products?id={id}` | Update product |
| DELETE | `/products?id={id}` | Delete product |

### Example API Request

**Create Product:**
```json
POST /products/
{
  "id": 5,
  "name": "Mouse",
  "description": "Wireless mouse",
  "price": 599.99,
  "quantity": 25
}
```

## UI Features

- **Powder Blue Theme** - Calming, professional color scheme
- **Gradient Backgrounds** - Modern visual appeal
- **Hover Effects** - Interactive table rows and buttons
- **Feature Pills** - Fast, Secure, Reliable
- **Real-time Search** - Instant filtering as you type

## CORS Configuration

The backend is configured to accept requests from `http://localhost:3000`. To modify this, update the CORS middleware in `main.py`:

```python
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"]
)
```

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Anusmaya**
- GitHub: [@anusmayaa](https://github.com/anusmayaa)

## Acknowledgments

- FastAPI documentation
- React documentation
- SQLAlchemy documentation

---

If you found this project helpful, please give it a star!
