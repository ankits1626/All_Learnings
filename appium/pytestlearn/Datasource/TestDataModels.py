from datetime import datetime
import html


class Merchant:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')


class Reward:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.terms_and_conditions = kwargs.get('terms_and_conditions')
        self.reward_description = kwargs.get('reward_description')
        self.valid_until = kwargs.get('valid_until')
        self.merchant = Merchant(**kwargs.get('merchant')) if kwargs.get('merchant') else None

    def formatted_valid_until(self):
        if self.valid_until:
            valid_until_datetime = datetime.fromisoformat(self.valid_until.split('T')[0])
            return valid_until_datetime.strftime("%d %B %Y")
        else:
            return None

    def get_terms_and_conditions(self):
        text = html.unescape(self.terms_and_conditions)

        text = text.replace("<p>", "\n").replace("</p>", "\n")
        text = text.replace("<ul>", "").replace("</ul>", "")
        text = text.replace("<li>", "\t•\t").replace("</li>", "\n")

        # Remove multiple consecutive newlines, then add a newline at the end
        text = '\n'.join([line for line in text.splitlines() if line.strip() != '']) + '\n'

        return text.strip('\n') + '\n'  # Ensure exactly one newline at the end


class RewardCategory:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.rewards = [Reward(**raw_reward) for raw_reward in kwargs.get('rewards', [])]


# Example usage:
raw_data = {
    "name": "Category Name",
    "rewards": [
        {
            "name": "Reward 1",
            "terms_and_conditions": """
<p>How to Redeem:</p>
<ul>
<li>Tap redeem &amp;&nbsp;follow instructions on the redeemed page to use promo code.</li>
</ul>
<p>Other T&amp;Cs:</p>
<ul>
<li>Not applicable on public holidays.</li>
</ul>
""",
            "reward_description": "Description for Reward 1",
            "valid_until": "2024-12-31",
            "merchant": {
                "name": "Merchant 1",
                "description": "Description for Merchant 1"
            }
        },
        {
            "name": "Reward 2",
            "terms_and_conditions": "T&C for Reward 2",
            "reward_description": "Description for Reward 2",
            "valid_until": "2024-12-31",
            "merchant": {
                "name": "Merchant 2",
                "description": "Description for Merchant 2"
            }
        }
    ]
}

category = RewardCategory(**raw_data)
print("Category Name:", category.name)
print("Rewards:")
for reward in category.rewards:
    print("  Reward Name:", reward.name)
    print("  Reward Description:", reward.reward_description)
    print("  tnc:", reward.get_terms_and_conditions())
    print("  Valid Until:", reward.formatted_valid_until())
    if reward.merchant:
        print("  Merchant Name:", reward.merchant.name)
        print("  Merchant Description:", reward.merchant.description)
