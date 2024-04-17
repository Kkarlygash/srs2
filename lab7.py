import asyncio

async def remove_spaces(s):
    await asyncio.sleep(1)
    return s.replace(" ", "")

async def to_lower_case(s):
    await asyncio.sleep(1)
    return s.lower()

async def remove_non_alphanumeric(s):
    await asyncio.sleep(1)
    return ''.join(char for char in s if char.isalnum())

async def compose(*functions):
    async def composed(arg):
        result = arg
        for func in functions:
            result = await func(result)
        return result
    return composed

async def process_string(input_string):
    string_processing = await compose(remove_spaces, to_lower_case, remove_non_alphanumeric)
    return await string_processing(input_string)

async def run_main():
    input_string = input("Жолды енгіз: ")
    output_string = await process_string(input_string)
    print(output_string)

asyncio.run(run_main())
