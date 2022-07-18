import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    ATTACKER_USERNAME = 'ATTACKER'
    ATTACKER_LEVEL = 10
    ATTACKER_HEALTH = 100
    ATTACKER_DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.attacker = Hero(self.ATTACKER_USERNAME, self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)
        # self.enemy = Hero(self.ATTACKER_USERNAME, self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

    def test_hero_init_correct(self):
        self.assertEqual(self.ATTACKER_USERNAME, self.attacker.username)
        self.assertEqual(self.ATTACKER_LEVEL, self.attacker.level)
        self.assertEqual(self.ATTACKER_DAMAGE, self.attacker.damage)
        self.assertEqual(self.ATTACKER_HEALTH, self.attacker.health)

    def test_battle_raises_when_attacker_and_enemy_with_same_name(self):
        enemy = Hero(self.ATTACKER_USERNAME, 5, 10, 20)

        with self.assertRaises(Exception) as ex:
            self.attacker.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_when_attacker_dead(self):
        enemy = Hero('name', 50, 10, 200)
        self.attacker.health = 0

        with self.assertRaises(ValueError) as ex:
            self.attacker.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raises_when_enemy_dead(self):
        enemy_username = "enemy"
        enemy = Hero(enemy_username, 50, 0, 200)

        with self.assertRaises(ValueError) as ex:
            self.attacker.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy_username}. He needs to rest", str(ex.exception))

    def test_battle_returns_draw_when_both_dead(self):
        enemy = Hero("enemy", self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self. ATTACKER_DAMAGE)

        result = self.attacker.battle(enemy)
        expected_health = self.ATTACKER_HEALTH - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)

        self.assertEqual('Draw', result)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_returns_win_when_enemy_dies(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10
        enemy = Hero("enemy", enemy_level, enemy_health, enemy_damage)

        result = self.attacker.battle(enemy)
        enemy_expected_health = enemy_health - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)
        attacker_expected_level = self.ATTACKER_LEVEL + self.BATTLE_LEVEL_INCREMENT
        attacker_expected_damage = self.ATTACKER_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        attacker_expected_health = self.ATTACKER_HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual('You win', result)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(attacker_expected_level, self.attacker.level)
        self.assertEqual(attacker_expected_damage, self.attacker.damage)
        self.assertEqual(attacker_expected_health, self.attacker.health)

    def test_battle_returns_defeat_when_attacker_dies(self):
        attacker_level, attacker_health, attacker_damage = 5, 100, 10
        attacker = Hero("attacker", attacker_level, attacker_health, attacker_damage)

        enemy = Hero("enemy", self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

        result = attacker.battle(enemy)
        attacker_expected_health = attacker_health - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)
        enemy_expected_level = self.ATTACKER_LEVEL + self.BATTLE_LEVEL_INCREMENT
        enemy_expected_damage = self.ATTACKER_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        enemy_expected_health = self.ATTACKER_HEALTH - (attacker_level * attacker_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual('You lose', result)
        self.assertEqual(attacker_expected_health, attacker.health)
        self.assertEqual(enemy_expected_level, enemy.level)
        self.assertEqual(enemy_expected_damage, enemy.damage)
        self.assertEqual(enemy_expected_health, enemy.health)

    def test_str_return_correct(self):
        actual = str(self.attacker)
        expected = f"Hero {self.ATTACKER_USERNAME}: {self.ATTACKER_LEVEL} lvl\n" \
            f"Health: {self.ATTACKER_HEALTH}\n" \
            f"Damage: {self.ATTACKER_DAMAGE}\n"

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
