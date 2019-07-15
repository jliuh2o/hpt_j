#!/usr/bin/env python

import alexandria as lib

character_stats = lib.stats()

lib.hp_calc(character_stats)

lib.combat_mop_up(character_stats)
