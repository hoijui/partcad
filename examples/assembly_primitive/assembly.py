#!/usr/bin/env python3
#
# OpenVMP, 2023
#
# Author: Roman Kuzmenko
# Created: 2023-08-19
#
# Licensed under Apache License, Version 2.0.
#

import partcad as pc

if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

part1 = pc.get_part("cube", "example_part_cadquery_primitive")
part2 = pc.get_part("cylinder", "example_part_cadquery_primitive")

model = pc.Assembly()
model.add(part1, loc=pc.Location((0, 0, 0), (0, 0, 1), 0))
model.add(part2, loc=pc.Location((0, 0, 5), (0, 0, 1), 0))
pc.finalize(model, show_object)
