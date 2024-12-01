import discord
from discord.ext import commands
import traceback

class EvalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="eval", help="Evaluates Python code (restricted to administrators).")
    @commands.has_permissions(administrator=True)
    async def eval_code(self, ctx, *, code: str):
        # Remove code block formatting
        code = code.strip("`")  # For cases where users wrap the code in backticks
        code = code.strip()

        # Define the function code
        func_code = (
            f"async def _eval_fn(ctx):\n"
            + "\n".join(f"    {line}" for line in code.splitlines())  # Indent the code for the function
        )

        try:
            # Execute the function definition
            local_vars = {"ctx": ctx}  # Ensure ctx is available inside the function
            exec(func_code, globals(), local_vars)

            # Call the function
            result = await local_vars["_eval_fn"](ctx)
            
            # Display the result
            if result is None:
                await ctx.send("`Code executed successfully with no output.`")
            else:
                await ctx.send(f"**Result:**\n```\n{result}\n```")
        except Exception as e:
            # Capture and display errors
            error_message = "".join(traceback.format_exception(type(e), e, e.__traceback__))
            await ctx.send(f"**Error:**\n```\n{error_message}\n```")

async def setup(bot):
    await bot.add_cog(EvalCog(bot))
