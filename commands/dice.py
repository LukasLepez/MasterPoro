"""
Regroup all Adventure Man dice commands 
"""

from discord.ext import commands
import random
import re

class Dice(commands.Cog):
    """ Regroup all language commands """

    @commands.command(description='Roll a dice (Example : $roll 1d100 | $roll 1d10+4)')
    async def roll(self, ctx, arg: str):
        """ Roll a dice (Example : $roll 1d100 / $roll 1d10+4) """

        author = ctx.message.author.name
        request = re.split('[d+/*-]', arg)

        number_dice = int(request[0])
        value_dice = int(request[1])

        if len(request) >= 3:
            additional_number = re.split('[+/*-]', arg, 1)[1]
            operator = re.split('([+/*-])', arg, 2)[1]
            additonal_value = additional_number
        else:
            additonal_value = None

        list_result = []
        min = 1
        i = 0

        while i < number_dice:
            i = i + 1
            result_dice = random.randint(min, value_dice)
            list_result.append(result_dice)

        list_result.sort()

        if additonal_value:
            sum_of_all_numbers= eval(str(sum(list_result)) + operator + additonal_value)
            if sum_of_all_numbers < 0:
                sum_of_all_numbers = 0

            calcul = str(eval(additonal_value))

            print(calcul)

            if float(calcul) < 0:
                add_value = re.split('([-])', calcul)[1] + ' ' + re.split('([-])', calcul)[2]
            else:
                add_value = operator + ' ' + calcul

        else:
            sum_of_all_numbers= sum(list_result)
            add_value = ''

        await ctx.send(f'**__{author} :__** ```{list_result} {add_value}``` \n **__Result :__** ```{sum_of_all_numbers}```')