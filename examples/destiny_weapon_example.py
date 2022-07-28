
from notion_operator_py import IntegrationClient


class DestinyWeapon:
    def __init__(self, auth: str):
        self.client = IntegrationClient(auth=auth)
        self.page = self.client.page()

    def new_record(self, title: str, season_url, weapon_type, category, perk1, perk2, perk3, perk4, cover, icon):
        _builder = self.page.new_builder()
        props = _builder.edit_properties(title_key="Name", title=title)
        props.add_file(key="Season", url=season_url)
        props.add_select(key="Type", select_name=weapon_type)
        props.add_select(key="Category", select_name=category)
        props.add_file(key="Perk#1", url=perk1)
        props.add_file(key="Perk#2", url=perk2)
        props.add_file(key="Perk#3", url=perk3)
        props.add_file(key="Perk#4", url=perk4)
        _builder.edit_cover(cover=cover)
        _builder.edit_icon(icon=icon)
        return _builder

    def submit(self, builder, parent_id, parent_type="database_id"):
        self.page.create(builder=builder, parent_id=parent_id, parent_type=parent_type)




if __name__ == '__main__':
    client = DestinyWeapon(auth="dwad")
    record = client.new_record(title="Snorri FR5",
                               season_url="https://bungie.net/common/destiny2_content/icons/d05833668bcb5ae25344dd4538b1e0b2.png",
                               weapon_type="Fusion Rifle",
                               category="EnergyWeapon",
                               perk1="https://bungie.net/common/destiny2_content/icons/7a0a23f9622636cea92387d50d368333.png",
                               perk2="https://bungie.net/common/destiny2_content/icons/fba0bbb5a21b74ebe59f394f2319098c.png",
                               perk3="https://bungie.net/common/destiny2_content/icons/ec51692c4a55ecf0b8a11065791bdc92.png",
                               perk4="https://bungie.net/common/destiny2_content/icons/68b82437cba6eeb5a215c2c8240861a5.png",
                               cover="https://bungie.net/common/destiny2_content/screenshots/4114929480.jpg",
                               icon="https://bungie.net/common/destiny2_content/icons/efd289a72ab64553dda6d6d5be92260a.jpg")
    client.submit(builder=record, parent_id="xxxxx")
