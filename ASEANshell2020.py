import os, sys, shutil, os.path

global countryName, selectCommand, listDirectory, changeDirectory, renameFile, copyFile, deleteFile
global createFile, readFile, appendFile, Exit, invalidCommand, blankInput, goodbye, enterDirectory, enterFile
global pathChanged, pathRestored, currentFilename, newFilename, filenameChanged, directoryFileNotExist
global currentFileCopy, newFileCopy, fileCopied, fileDeleted, createName, fileCreated, fileExists
global writeContent, fileUpdated, deleteFileText

command = '0'


# MAIN FUNCTION -----------------------------------------------------

def main():
    global command
    # Select country/language
    country = input("""
    Welcome to ASEANshell!

    Please select your country.
    1. Malaysia
    2. Philippines
    3. Thailand
    """)
    country = str(country)

    while command != '9':
        # language
        if country == '1':
            malaysia()

        elif country == '2':
            philippines()

        elif country == '3':
            thailand()

        else:
            print('Invalid command')
            exit()

        command = input(
            f"You are from {countryName}\n"

            f"Select command - {selectCommand}\n"

            f"1. List directory - {listDirectory}\n"
            f"2. Change directory - {changeDirectory}\n"
            f"3. Rename file - {renameFile}\n"
            f"4. Copy file - {copyFile}\n"
            f"5. Delete file - {deleteFile}\n"
            f"6. Create file - {createFile}\n"
            f"7. Read file - {readFile}\n"
            f"8. Append file - {appendFile}\n"
            f"9. Exit - {Exit}\n"

        )
        command = str(command)

        # Carry out command
        # List directory
        if command == '1':
            list_directory()

        # Change directory
        elif command == '2':
            change_directory()

        # Change file name
        elif command == '3':
            change_filename()

        # Copy file
        elif command == '4':
            copy_file()

        # Delete file
        elif command == '5':
            delete_file()

        # Create file
        elif command == '6':
            create_file()

        # Read file
        elif command == '7':
            read_file()

        # Append file
        elif command == '8':
            append_file()


        # Invalid input
        elif command != '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8':
            if command != '9':
                print(invalidCommand)
                blank = input(blankInput)

    # Exit
    else:
        print(goodbye)
        exit()


# -------------------------------------------------------------------------------------


# COMMANDS -----------------------------------------------------------------------
def list_directory():
    os.system('ls')
    blank = input(blankInput)


def change_directory():
    directory = input(enterDirectory)

    # exception for invalid directory
    try:
        os.chdir(directory)
        cwd = os.getcwd()
        print(pathChanged + cwd)
    except:
        print(directoryFileNotExist, sys.exc_info())
        cwd = os.getcwd()
        os.chdir(cwd)
        print(pathRestored + cwd)
    blank = input(blankInput)


def change_filename():
    # exception for invalid file name/directory
    try:
        currentName = input(currentFilename)
        newName = input(newFilename)
        os.rename(currentName, newName)
        print(filenameChanged)
    except:
        print(directoryFileNotExist, sys.exc_info())
    blank = input(blankInput)


def copy_file():
    # exception for invalid file
    try:
        currentCopy = input(currentFileCopy)
        newCopy = input(newFileCopy)
        shutil.copy2(currentCopy, newCopy)
        print(fileCopied)
    except:
        print(directoryFileNotExist, sys.exc_info())
    blank = input(blankInput)


def delete_file():
    # exception for invalid file
    try:
        deleteFileText = input(deleteFile)
        os.remove(deleteFileText)
        print(fileDeleted)
    except:
        print(directoryFileNotExist, sys.exc_info())
    blank = input(blankInput)


def create_file():
    # exception for file that already exist
    createFileName = input(createName)
    if os.path.exists(createFileName):
        print(fileExists)
    elif createFileName == '':
        print(invalidCommand)
    else:
        open(createFileName, 'w').close()
        print(fileCreated)
    blank = input(blankInput)


def read_file():
    # exception for invalid file name
    try:
        readFileName = input(createName)
        fileContents = open(readFileName, 'r')
        print(fileContents.read())
        fileContents.close()
    except:
        print(directoryFileNotExist, sys.exc_info())
    blank = input(blankInput)


def append_file():
    # exception for invalid file name
    writeFileName = input(createName)
    writeTextName = input(writeContent)
    if os.path.exists(writeFileName):
        writeFileContents = open(writeFileName, 'a')
        writeFileContents.write("\n" + writeTextName)
        writeFileContents.close()
        print(fileUpdated)
    else:
        print(directoryFileNotExist)
    blank = input(blankInput)


# ----------------------------------------------------------------------------------------


# LANGUAGES -------------------------------------------------------------------------------
def malaysia():
    global countryName, selectCommand, listDirectory, changeDirectory, renameFile, copyFile, deleteFile
    global createFile, readFile, appendFile, Exit, invalidCommand, blankInput, goodbye, enterDirectory, enterFile
    global pathChanged, pathRestored, currentFilename, newFilename, filenameChanged, directoryFileNotExist
    global currentFileCopy, newFileCopy, fileCopied, deleteFile, fileDeleted, createName, fileCreated, fileExists
    global writeContent, fileUpdated, deleteFileText
    countryName = 'Malaysia'
    selectCommand = 'Pilih arahan'
    listDirectory = 'Senarai Direktori'
    changeDirectory = 'Tukar Direktori'
    renameFile = 'Tukar nama fail'
    copyFile = 'Salin fail'
    deleteFile = 'Padam fail'
    createFile = 'Buat fail'
    readFile = 'Baca fail'
    appendFile = 'Tambah fail'
    Exit = 'Keluar'
    invalidCommand = 'Perintah tidak sah'
    blankInput = 'Tekan "enter" untuk meneruskan'
    goodbye = 'Selamat tinggal!'
    enterDirectory = 'Masukkan direktori'
    enterFile = 'Masukkan fail'
    pathChanged = 'Laluan berubah, direktori sekarang:'
    pathRestored = 'Laluan dipulihkan, direktori sekarang:'
    currentFilename = 'Direktori fail dan nama semasa:'
    newFilename = 'Direktori fail baru, nama dan jenis:'
    filenameChanged = 'Nama fail diubah'
    directoryFileNotExist = 'Direktori atau fail tidak wujud'
    currentFileCopy = 'Direktori dan fail untuk disalin:'
    newFileCopy = 'Direktori baru dan nama fail yang disalin:'
    fileCopied = 'Fail disalin'
    deleteFile = 'Direktori dan fail yang hendak dipadamkan:'
    fileDeleted = 'Fail dipadam'
    createName = 'Masukkan nama fail:'
    fileCreated = 'Fail dibuat'
    fileExists = 'Nama fail sudah wujud, fail tidak dibuat'
    writeContent = 'Tulis teks:'
    fileUpdated = 'Fail dikemas kini'


def philippines():
    global countryName, selectCommand, listDirectory, changeDirectory, renameFile, copyFile, deleteFile
    global createFile, readFile, appendFile, Exit, invalidCommand, blankInput, goodbye, enterDirectory, enterFile
    global pathChanged, pathRestored, currentFilename, newFilename, filenameChanged, directoryFileNotExist
    global currentFileCopy, newFileCopy, fileCopied, deleteFile, fileDeleted, createName, fileCreated, fileExists
    global writeContent, fileUpdated, deleteFileText
    countryName = 'Philippines'
    selectCommand = 'Piliin ang utos'
    listDirectory = 'Listahan ng direktoryo'
    changeDirectory = 'Baguhin ang direktoryo'
    renameFile = 'Palitan ANG pangalan ng file'
    copyFile = 'Kopyahin ang file'
    deleteFile = 'Burahin ang file'
    createFile = 'Lumikha ng file'
    readFile = 'Basahin ang file'
    appendFile = 'Magdagdag ng file'
    Exit = 'Labasan'
    invalidCommand = 'Di-wastong utos'
    blankInput = 'Pindutin ang ipasok upang magpatuloy'
    goodbye = 'Paalam!'
    enterDirectory = 'Ipasok ang direktoryo'
    enterFile = 'Ipasok ang file'
    pathChanged = 'Nagbago ang landas, kasalukuyang direktoryo:'
    pathRestored = 'Naibalik ang landas, direktoryo ng kasalukuyan:'
    currentFilename = 'Kasaysayan ng direktoryo at pangalan:'
    newFilename = 'Bagong direktoryo ng pangalan, pangalan at uri:'
    filenameChanged = 'Nabago ang pangalan ng file'
    directoryFileNotExist = 'Ang direktoryo o file ay hindi umiiral'
    currentFileCopy = 'Direktoryo at file na makopya:'
    newFileCopy = 'Bagong direktoryo at kinopyang pangalan ng file:'
    fileCopied = 'Nakopya ang file'
    deleteFile = 'Directory at file na tatanggalin:'
    fileDeleted = 'Natanggal ang file'
    createName = 'Ipasok ang pangalan ng file:'
    fileCreated = 'Nilikha ang file'
    fileExists = 'Ang pangalan ng file ay mayroon na, hindi nilikha ang file'
    writeContent = 'Sumulat ng teksto:'
    fileUpdated = 'Nai-update ang file'


def thailand():
    global countryName, selectCommand, listDirectory, changeDirectory, renameFile, copyFile, deleteFile
    global createFile, readFile, appendFile, Exit, invalidCommand, blankInput, goodbye, enterDirectory, enterFile
    global pathChanged, pathRestored, currentFilename, newFilename, filenameChanged, directoryFileNotExist
    global currentFileCopy, newFileCopy, fileCopied, deleteFile, fileDeleted, createName, fileCreated, fileExists
    global writeContent, fileUpdated, deleteFileText
    countryName = 'Thailand'
    selectCommand = 'เลือกคำสั่ง'
    listDirectory = 'รายการไดเรกทอรี'
    changeDirectory = 'เปลี่ยนไดเรกทอรี'
    renameFile = 'เปลี่ยนชื่อไฟล์'
    copyFile = 'คัดลอกไฟล์'
    deleteFile = 'ลบไฟล์'
    createFile = 'สร้างไฟล์'
    readFile = 'อ่านไฟล์'
    appendFile = 'ต่อท้ายไฟล์'
    Exit = 'ทางออก'
    invalidCommand = 'คำสั่งไม่ถูกต้อง'
    blankInput = 'กด"Enter"เพื่อดำเนินการต่อ'
    goodbye = 'ลาก่อน!'
    enterDirectory = 'เข้าสู่ไดเรกทอรี'
    enterFile = 'ใส่ไฟล์'
    pathChanged = 'เปลี่ยนเส้นทางนำเสนอไดเรกทอรี:'
    pathRestored = 'เส้นทางที่คืนค่าไดเรกทอรีปัจจุบัน:'
    currentFilename = 'ไดเรกทอรีและชื่อไฟล์ปัจจุบัน:'
    newFilename = 'ไดเรกทอรีไฟล์ใหม่ชื่อและประเภท:'
    filenameChanged = 'เปลี่ยนชื่อไฟล์แล้ว'
    directoryFileNotExist = 'ไม่มีไดเรกทอรีหรือไฟล์'
    currentFileCopy = 'ไดเรกทอรีและไฟล์ที่จะคัดลอก:'
    newFileCopy = 'ไดเรกทอรีใหม่และชื่อไฟล์ที่คัดลอก:'
    fileCopied = 'คัดลอกไฟล์แล้ว'
    deleteFile = 'ไดเรกทอรีและไฟล์ที่จะลบ:'
    fileDeleted = 'ไฟล์ถูกลบ'
    createName = 'ใส่ชื่อไฟล์:'
    fileCreated = 'สร้างไฟล์แล้ว'
    fileExists = 'มีชื่อไฟล์อยู่แล้วไฟล์ไม่ได้ถูกสร้างขึ้น'
    writeContent = 'เขียนข้อความ:'
    fileUpdated = 'อัปเดตไฟล์แล้ว'


# ------------------------------------------------------------------------------------

# main function call
main()
