from abc import abstractmethod
from typing import List
from ..models import Member, Status


class Voting:
    vote_options: List[str]
    # Could merge these variables in a dict but would be unsafe for privacy
    members_voted: List[Member]
    votes: dict[str, int]

    def __init__(self, options: List[str]):
        self.vote_options = options
        self.members_voted = []
        # Init every option with 0 votes
        self.votes = {opt: 0 for opt in options}

    @abstractmethod
    def can_vote(self, member: Member) -> bool:
        pass

    def vote(self, *, member: Member, option: str) -> None:
        if self.can_vote(member):
            self.members_voted.append(member)
            self.votes[option] += 1


class VoteByStatus(Voting):
    allowed_statuses: List[Status]

    def __init__(self, options: List[str], voting_status: List[Status]):
        super().__init__(options)
        self.allowed_statuses = voting_status

    def can_vote(self, member: Member) -> bool:
        return member.status in self.allowed_statuses


class VoteByMember(Voting):
    allowed_members: List[Member]

    def __init__(self, options: List[str], voting_members: List[Member]):
        super().__init__(options)
        self.allowed_members = voting_members

    def can_vote(self, member: Member) -> bool:
        return member.id in self.allowed_members
