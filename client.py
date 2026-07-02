from typing import Dict, Any, List

class SplitShipmentClient:
    def plan_delivery(self, cart: List[dict], warehouse_inventory: Dict[str, List[str]]) -> Dict[str, Any]:
        # warehouse_inventory like {"Whse_A": ["item1", "item2"], "Whse_B": ["item3"]}
        allocation = {}
        split_count = 0
        for item in cart:
            sku = item.get("sku")
            allocated = False
            for whse, items in warehouse_inventory.items():
                if sku in items:
                    allocation.setdefault(whse, []).append(sku)
                    allocated = True
                    break
            if not allocated:
                allocation.setdefault("backorder", []).append(sku)
        split_count = len([k for k in allocation if len(allocation[k]) > 0])
        return {
            "shipping_plan": allocation,
            "split_shipments_needed": max(1, split_count)
        }
