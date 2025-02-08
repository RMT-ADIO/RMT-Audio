def remote(a,b,c):
    r =  "Not Yet, Wait a minute, sir!"
    return r

import asyncio
from bleak import BleakClient

# 블루투스 장치의 MAC 주소
DEVICE_ADDRESS = "00:11:22:33:44:55"  # 연결하려는 장치의 실제 주소로 변경

def print_menu():
    print("\n--- Bluetooth Control ---")
    print("1. 연결")
    print("2. 연결 해제")
    print("3. 종료")

async def connect_and_disconnect():
    client = BleakClient(DEVICE_ADDRESS)

    while True:
        print_menu()
        choice = input("메뉴 선택: ")

        if choice == "1":
            try:
                print("장치에 연결 중...")
                await client.connect()
                if client.is_connected:
                    print(f"장치에 연결됨: {DEVICE_ADDRESS}")
                else:
                    print("연결 실패")
            except Exception as e:
                print(f"연결 중 오류 발생: {e}")

        elif choice == "2":
            try:
                if client.is_connected:
                    print("장치 연결 해제 중...")
                    await client.disconnect()
                    print("연결 해제 완료")
                else:
                    print("이미 연결이 해제되어 있습니다.")
            except Exception as e:
                print(f"연결 해제 중 오류 발생: {e}")

        elif choice == "3":
            print("프로그램 종료.")
            if client.is_connected:
                await client.disconnect()
            break

        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

# asyncio를 사용해 main 함수 실행
asyncio.run(connect_and_disconnect())

