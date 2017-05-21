import functions as f
import psycopg2
import os


def main():
    while True:
        f.print_menu()
        user_input = int(input('Choose an option: '))
        os.system('clear')
        if user_input == 0:
            quit()
        elif user_input == 1:
            f.print_result(f.connection(f.mentors_name()))
        elif user_input == 2:
            f.print_result(f.connection(f.mentors_nickname()))
        elif user_input == 3:
            f.print_result(f.connection(f.carols_datas()))
        elif user_input == 4:
            f.print_result(f.connection(f.other_girls_datas()))
        elif user_input == 5:
            for datas in f.connection(f.show_all_applicants()):
                if 54823 in datas:
                    is_in_list = True
            if is_in_list:
                print('This applicant is already exists.\n')
                f.print_result(f.connection(f.show_new_applicant()))
            else:
                f.modify_database(f.insert_new_applicant())
                f.print_result(f.connection(f.show_new_applicant()))
        elif user_input == 6:
            f.modify_database(f.update_phone_number())
            f.print_result(f.connection(f.show_updated_number()))
        elif user_input == 7:
            f.modify_database(f.delete_applicants())
            f.print_result(f.connection(f.show_all_applicants()))
        elif user_input == 8:
            f.print_result(f.connection(f.show_all_mentors()))
        elif user_input == 9:
            f.print_result(f.connection(f.show_all_applicants()))
        else:
            pass


if __name__ == '__main__':
    main()
