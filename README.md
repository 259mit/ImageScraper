# ImageScraper

### Tired of searching and downloading multiple images for your project or presentation? ImageScraper is a one stop solution to extracting images for multiple keywords!

## Steps to install and use ImageScraper

### Installation

1. Install Google Chrome
-   https://www.google.com/chrome/

2. Install Chrome Driver for your Chrome version
-   To check Chrome version:
-   Chrome>More(three vertical dots on top right)>Help>About Google Chrome
-   For MAC OS users with Chrome v91: Install driver from the repository
-   Else: Install driver for your OS: 
-    https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.101/

3. Install Requirements from 'requirements.txt'

### Using ImageScraper

1. List Keywords you need to search images in an excel sheet
2. Specify sheet path and keywords column name
3. Specify number of images needed per keyword
4. Specify Chrome Driver path
5. Run 'ImageScraper.py'
 - Optional: Run main.py
6. Images are saved in a directory IMAGES with pwd as the directory of Chrome Driver. Each keyword has a subdirectory within IMAGES and saves images as a .jpg file.

Mithesh Ramachandran
