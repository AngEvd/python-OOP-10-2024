from project.hero import Hero

import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Test", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_init(self):
        self.assertEqual(self.hero.username, "Test")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_self(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual(str(context.exception), 'You cannot fight yourself')

    def test_battle_with_no_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_battle_enemy_with_no_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), 'You cannot fight Enemy. He needs to rest')

    def test_battle_and_draw(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)
        self.assertEqual(result, 'Draw')
        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

    def test_battle_and_win(self):
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual(result, 'You win')
        self.assertEqual(self.hero.level, expected_level)
        self.assertEqual(self.hero.health, expected_health)
        self.assertEqual(self.hero.damage, expected_damage)

    def test_battle_and_lose(self):
        self.hero, self.enemy = self.enemy, self.hero

        expected_level = self.enemy.level + 1
        expected_health = self.enemy.health - self.hero.damage + 5
        expected_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual(result, 'You lose')
        self.assertEqual(self.enemy.level, expected_level)
        self.assertEqual(self.enemy.health, expected_health)
        self.assertEqual(self.enemy.damage, expected_damage)

    def test_str(self):
        self.hero.level = 5
        self.hero.health = 100
        self.hero.damage = 100

        result = self.hero.__str__()
        expected_result = f"Hero Test: 5 lvl\nHealth: 100\nDamage: 100\n"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
