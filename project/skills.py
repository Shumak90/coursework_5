from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Any, Type

if TYPE_CHECKING:
    from project.unit import BaseUnit


class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def damage(self) -> float:
        pass

    @property
    @abstractmethod
    def stamina(self) -> float:
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self) -> float:
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryPunch(Skill):
    name: str = "Свирепый пинок"
    stamina: float = 6
    damage: float = 12

    def skill_effect(self) -> str:
        # логика использования скилла -> return str
        # в классе нам доступны экземпляры user и target - можно использовать любые их методы
        # именно здесь происходит уменшение стамины у игрока применяющего умение и
        # уменьшение здоровья цели.
        # результат применения возвращаем строкой
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона"


class HardShot(Skill):
    name: str = "Мощный укол"
    stamina: float = 5
    damage: float = 15

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона"
