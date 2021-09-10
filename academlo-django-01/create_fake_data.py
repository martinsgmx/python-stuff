#!/usr/env/python3
import sqlite3


students: list = [
    {
        'name': 'Adrian',
        'lastname': 'Boss',
        'born_date': '1979-08-12',
        'nationality': 'US',
        'profile_pic': 'https://cdn4.iconfinder.com/data/icons/professions-1-2/151/8-512.png',
        'email': 'adrian@email.edu'
    },
    {
        'name': 'Mariam',
        'lastname': 'Dress',
        'born_date': '1991-04-10',
        'nationality': 'GB',
        'profile_pic': 'https://cdn4.iconfinder.com/data/icons/professions-1-1/128/25-512.png',
        'email': 'mariam@email.edu'
    },
    {
        'name': 'Steffy',
        'lastname': 'Brown',
        'born_date': '1994-06-10',
        'nationality': 'CA',
        'profile_pic': 'https://cdn4.iconfinder.com/data/icons/professions-1-1/128/25-512.png',
        'email': 'steffy@email.edu'
    },
    {
        'name': 'Robert',
        'lastname': 'De Niro',
        'born_date': '1992-12-03',
        'nationality': 'FR',
        'profile_pic': 'https://cdn4.iconfinder.com/data/icons/professions-1-2/151/8-512.png',
        'email': 'robert@email.edu'
    },
]


courses: list = [
    {
        'about': 'Maths and algorithms.',
        'duration': 4,
        'name': 'Math',
        'url_cover': 'https://wallpapercave.com/wp/WpwaASb.jpg'
    },
    {
        'about': 'Chemistry organic.',
        'duration': 6,
        'name': 'Chemistry',
        'url_cover': 'https://wallpapercave.com/wp/RArQux4.jpg'
    },
    {
        'about': 'Computer science and programming.',
        'duration': 6,
        'name': 'Computer Science',
        'url_cover': 'https://wallpapercave.com/wp/wp2105387.jpg'
    },
    {
        'about': 'History and culture.',
        'duration': 3,
        'name': 'History',
        'url_cover': 'https://getwallpapers.com/wallpaper/full/c/7/f/341339.jpg'
    },
]


def create_course(about: str, duration: int, name: str, url_cover: str) -> None:
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO courses_course (about, duration, name, url_image, is_active)
    VALUES (?, ?, ?, ?, ?);""", (about, duration, name, url_cover, True))

    conn.commit()
    conn.close()


def create_student(name: str, lastname: str, born_date: str, nationality: str, profile_pic: str, email: str) -> None:
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO students_student (name, lastname, born_date, nationality, profile_pic, email, is_active)
    VALUES (?, ?, ?, ?, ?, ?, ?);""", (name, lastname, born_date, nationality, profile_pic, email, True))

    conn.commit()
    conn.close()


def main() -> None:
    for course in courses:
        create_course(course['about'], course['duration'], course['name'], course['url_cover'])

    for student in students:
        create_student(student['name'], student['lastname'], student['born_date'], student['nationality'], student['profile_pic'], student['email'])


if __name__ == "__main__":
    main()

#  to absent friends
