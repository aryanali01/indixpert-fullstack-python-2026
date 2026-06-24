import json
import os



# ================= READ DATA =================

def read_data(file_path):

    try:

        # agar file nahi hai
        if not os.path.exists(file_path):

            return {}



        with open(
            file_path,
            "r"
        ) as file:


            data = json.load(file)


            return data




    except json.JSONDecodeError:


        print(
            f"\n[ERROR] Invalid JSON Format : {file_path}"
        )


        return {}





    except Exception as e:


        print(
            f"\n[ERROR] {e}"
        )


        return {}







# ================= WRITE DATA =================


def write_data(file_path, data):

    try:


        # folder check

        folder = os.path.dirname(file_path)



        if folder and not os.path.exists(folder):

            os.makedirs(folder)




        with open(
            file_path,
            "w"
        ) as file:


            json.dump(
                data,
                file,
                indent=4
            )




        print(
            "\n[SUCCESS] Data Saved Successfully"
        )





    except Exception as e:


        print(
            f"\n[ERROR] {e}"
        )