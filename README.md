git ad# Google Search Analysis

A web application for analyzing Google search results.

## Features
- Search Google using custom search API
- Analyze search results
- Save search history
- User authentication

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Set up environment variables in `.env` file
4. Run the application:
   ```bash
   python backend/app.py
   ```

## Configuration
Create a `.env` file with the following variables:
```
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
GOOGLE_API_KEY=your_api_key
SEARCH_ENGINE_ID=your_engine_id
SECRET_KEY=your_secret_key
```

## Usage
1. Access the application at `http://localhost:5000`
2. Create an account or login
3. Enter search queries and view results
4. Analyze search history in the dashboard

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
