from uAgents.src.uagents import Agent, Context, Model
from aumanaque import Create_agent
from action import Action

class Message(Model):
    message: str
    
agent1 = Create_agent.Agent1()
action = Action()
  
@agent1.on_event('startup')
async def plan_event(ctx: Context):
    agent1.desire(ctx, 'initial_desire')
    
    agent1.belief(ctx, "opening", True)
    agent1.belief(ctx, "symbol", "None")
    agent1.belief(ctx, "price_min_check", False)
    agent1.belief(ctx, "price_max_check", False)
    
    agent1.set_plan_library(ctx, "min", {"price_min_check": True}, ["get_min"])
    agent1.set_plan_library(ctx, "max", {"price_max_check": True}, ["get_max"])
    agent1.set_plan_library(ctx, "day_trade", {"opening": True}, ["trade", "check_buyorsell", "check_upordown", "check_wallet", "check_price"])
    agent1.set_plan_library(ctx, "analytic", {"opening": True}, ["day_trade", "max", "check_max", "min", "check_min", "get_symbol"])

@agent1.on_interval(period=10.5)
async def plan_interval(ctx: Context):
    agent1.desire(ctx, 'analytic') if agent1.contexto(ctx, {"opening": True}) else False
    agent1.update_intention(ctx)
    action.sell(ctx) if agent1.contexto(ctx, {"sell": True}) else False
    action.buy(ctx) if agent1.contexto(ctx, {"buy": True}) else False

@agent1.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from: {msg.message}")
    if msg.message == 'opening':
        agent1.belief(ctx, "opening", True)
        agent1.belief(ctx, "symbol", "None")
        agent1.belief(ctx, "price_min_check", True)
        agent1.belief(ctx, "price_max_check", True)
    elif msg.message == 'closing':
        agent1.belief(ctx, "opening", False)
        agent1.belief(ctx, "symbol", "None")
        agent1.belief(ctx, "price_min_check", False)
        agent1.belief(ctx, "price_max_check", False)
        action.closing_check(ctx)
    
if __name__ == "__main__":
    agent1.run()
