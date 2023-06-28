from pyrogram import Client
import asyncio

async def stringGenerate():
    api_id = input("Api ID: \n")
    api_hash = input("Api Hash: \n")
    client = Client(":memory:", api_id, api_hash)
    await client.connect()
    
    phone_number = input("Insert your phone number: \n")
    print("Sending code to telegram... \n")
    code = await client.send_code(phone_number)
    
    phone_code_msg = input("Insert registration code: \n")
    
    await client.sign_in(phone_number, code.phone_code_hash, phone_code_msg)
    
    bolean = input("You have double factor? y/n \n")
    
    if bolean == 'y':
        password = input('Insert your double factor:\n')
        await client.check_password(password=password)
        
    
    
    string_session = await client.export_session_string()
    
    
    print(f"Session String:\n{string_session}")
    
    
if __name__ == "__main__":
    asyncio.run(stringGenerate())