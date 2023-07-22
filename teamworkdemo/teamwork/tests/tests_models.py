from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from teamwork.models import Profile, Group, Member, ProfileForm


class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        user = User.objects.create(username='testuser')
        profile = Profile.objects.create(user=user)
        self.assertEqual(profile.user, user)


class GroupModelTest(TestCase):
    def test_group_creation(self):
        user = User.objects.create(username='testuser')
        group = Group.objects.create(name='Test Group', admin=user)
        self.assertEqual(group.name, 'Test Group')
        self.assertEqual(group.admin, user)


class MemberModelTest(TestCase):
    def test_member_creation(self):
        user = User.objects.create(username='testuser')
        group = Group.objects.create(name='Test Group', admin=user)
        member = Member.objects.create(member=user, group=group)
        self.assertEqual(member.member, user)
        self.assertEqual(member.group, group)


class BelbinUserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.group = Group.objects.create(name='Test Group', admin=self.user)
        self.member = Member.objects.create(member=self.user, group=self.group)

    def test_belbin_user_profile_results(self):
        belbin_profile = ProfileForm.objects.create(
            member=self.member,
            resource_investigator=1,
            team_worker=2,
            coordinator=3,
            plant=4,
            monitor_evaluator=5,
            specialist=6,
            shaper=7,
            implementer=8,
            completer_finisher=9
        )

        expected_results = [
            'completer_finisher'
        ]

        self.assertEqual(belbin_profile.primary_roles(), expected_results)
