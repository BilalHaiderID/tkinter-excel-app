# Tkinter Excel App

A Python desktop application that provides a graphical user interface (GUI) for managing employee data stored in Excel spreadsheets. Built with **Tkinter** and **openpyxl**, this application allows users to view, insert, and organize personnel information with an intuitive interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## Features

✨ **Key Features:**
- 📊 **View Employee Data** - Display employee records in a scrollable table
- ➕ **Insert New Records** - Add employee data (Name, Age, Subscription Status, Employment Status)
- 💾 **Excel Integration** - Seamless read/write operations with `.xlsx` files
- 🎨 **Dark/Light Theme** - Toggle between modern forest-dark and forest-light themes
- 📋 **Subscription Management** - Track subscription status (Subscribed, Not Subscribed, Other)
- ✔️ **Employment Status** - Record employment status with checkbox
- 🔄 **Real-time Updates** - Automatic table refresh after data insertion

## Screenshots

![App Demo](screenshots/app-demo.png)

*Excel Data Manager with Dark Theme - View and manage employee records effortlessly*

## Prerequisites

- **Python 3.7** or higher
- **pip** (Python package manager)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/BilalHaiderID/tkinter-excel-app.git
cd tkinter-excel-app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create Data Directory
```bash
mkdir -p people
```

### 4. Create Sample Excel File (Optional)
If you want to use sample data, create `people/people.xlsx` with the following columns:
- Name
- Age
- Subscription
- Employment

## Usage

### Run the Application
```bash
python main.py
```

### How to Use

1. **Insert Employee Data:**
   - Enter the employee's name in the "Name" field
   - Select age using the spinbox (18-100)
   - Choose subscription status from the dropdown (Subscribed, Not Subscribed, Other)
   - Check "Employed" if applicable
   - Click "Insert" to add the record

2. **View Data:**
   - All employee records are displayed in the table on the right
   - Use the scrollbar to navigate through records
   - Columns show: Name, Age, Subscription, Employment

3. **Switch Theme:**
   - Toggle "Light Mode" checkbox to switch between dark and light themes
   - Default theme is dark mode

## File Structure

```
tkinter-excel-app/
├── main.py                 # Main application file
├── requirements.txt        # Project dependencies
├── LICENSE                 # MIT License
├── README.md              # This file
├── forest-dark.tcl        # Dark theme configuration
├── forest-light.tcl       # Light theme configuration
├── people/                # Data directory
│   └── people.xlsx        # Excel file with employee data
└── screenshots/           # Screenshot directory
    └── app-demo.png       # Application screenshot
```

## Project Structure Details

### Main Components

**main.py**
- `lighttheme()` - Handles theme switching between dark and light modes
- `load_data()` - Loads employee data from Excel file into the table
- `insert_data()` - Inserts new employee records into the Excel file
- GUI Components: Entry fields, Combobox, Checkbutton, Treeview, Scrollbar

**Theme Files**requirements.txt

- `forest-dark.tcl` - Modern dark theme styling
- `forest-light.tcl` - Modern light theme styling

**Data Storage**
- `people/people.xlsx` - Excel spreadsheet containing employee records

## Requirements

```
openpyxl==3.10.1
```

**Note:** Tkinter comes bundled with Python and doesn't need to be installed separately.

## Configuration

### Data File Path
The default data file location is `people/people.xlsx`. To change this:

1. Open `main.py`
2. Modify the `path` variable:
```python
path = "your/custom/path/data.xlsx"
```

### Column Configuration
To modify the table columns, edit the `coldata` variable in `main.py`:
```python
coldata = ("Name", "Age", "Subscription", "Employment")
```

## Troubleshooting

### Excel File Not Found
- **Error:** `FileNotFoundError: people/people.xlsx`
- **Solution:** Create the `people` directory and `people.xlsx` file with proper headers

### Theme Files Missing
- **Error:** `TCL Error: couldn't read file "forest-dark.tcl"`
- **Solution:** Ensure `forest-dark.tcl` and `forest-light.tcl` are in the root directory

### Age Entry Error
- **Error:** `ValueError: invalid literal for int()`
- **Solution:** Ensure the age field contains a valid number between 18-100

### openpyxl Not Installed
- **Error:** `ModuleNotFoundError: No module named 'openpyxl'`
- **Solution:** Run `pip install -r requirements.txt`

## Future Enhancements

🚀 **Planned Features:**
- [ ] Delete employee records
- [ ] Edit existing records
- [ ] Search/Filter functionality
- [ ] Export to PDF
- [ ] Data validation and error handling
- [ ] Database integration (SQLite/MySQL)
- [ ] Multi-file management
- [ ] Backup and restore functionality

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Author

**BilalHaiderID**
- GitHub: [@BilalHaiderID](https://github.com/BilalHaiderID)

## Support

If you encounter any issues or have suggestions, please:
- Open an [Issue](https://github.com/BilalHaiderID/tkinter-excel-app/issues)
- Create a [Discussion](https://github.com/BilalHaiderID/tkinter-excel-app/discussions)

## Acknowledgments

- Forest Theme by [rdbende](https://github.com/rdbende/Forest-ttk-theme)
- openpyxl library for Excel file handling
- Python Tkinter for GUI framework

---

**Last Updated:** 2026-04-01  
