from gw2api.objects.base_object import BaseAPIObject


class BaseAPIv2Object(BaseAPIObject):
    """Extends the base API handler to automatically handle pagination and id parameters"""

    def get(self, **kwargs):
        return super().get(id=kwargs.get('id'),
                           ids=kwargs.get('ids'),
                           url=kwargs.get('url'),
                           page=kwargs.get('page'),
                           page_size=kwargs.get('page_size')).json()


class Account(BaseAPIv2Object):
    pass


class AccountAchievements(BaseAPIv2Object):
    pass


class AccountBank(BaseAPIv2Object):
    pass


class AccountBuildStorage(BaseAPIv2Object):
    pass


class AccountDailyCrafting(BaseAPIv2Object):
    pass


class AccountDungeons(BaseAPIv2Object):
    pass


class AccountDyes(BaseAPIv2Object):
    pass


class AccountEmotes(BaseAPIv2Object):
    pass


class AccountFinishers(BaseAPIv2Object):
    pass


class AccountGliders(BaseAPIv2Object):
    pass


class AccountHome(BaseAPIv2Object):
    pass


class AccountHomeCats(BaseAPIv2Object):
    pass


class AccountHomeNodes(BaseAPIv2Object):
    pass


class AccountInventory(BaseAPIv2Object):
    pass


class AccountLuck(BaseAPIv2Object):
    pass


class AccountMail(BaseAPIv2Object):
    pass


class AccountMailCarriers(BaseAPIv2Object):
    pass


class AccountMapChests(BaseAPIv2Object):
    pass


class AccountMasteries(BaseAPIv2Object):
    pass


class AccountMasteryPoints(BaseAPIv2Object):
    pass


class AccountMaterials(BaseAPIv2Object):
    pass


class AccountMinis(BaseAPIv2Object):
    pass


class AccountMounts(BaseAPIv2Object):
    pass


class AccountMountsSkins(BaseAPIv2Object):
    pass


class AccountMountsTypes(BaseAPIv2Object):
    pass


class AccountNovelties(BaseAPIv2Object):
    pass


class AccountOutfits(BaseAPIv2Object):
    pass


class AccountPvPHeroes(BaseAPIv2Object):
    pass


class AccountRaids(BaseAPIv2Object):
    pass


class AccountRecipes(BaseAPIv2Object):
    pass


class AccountSkins(BaseAPIv2Object):
    pass


class AccountTitles(BaseAPIv2Object):
    pass


class AccountWallet(BaseAPIv2Object):
    pass


class AccountWorldBosses(BaseAPIv2Object):
    pass


class Achievements(BaseAPIv2Object):
    pass


class AchievementsCategories(BaseAPIv2Object):
    pass


class AchievementsDaily(BaseAPIv2Object):
    pass


class AchievementsDailyTomorrow(BaseAPIv2Object):
    pass


class AchievementsGroups(BaseAPIv2Object):
    pass


class Adventures(BaseAPIv2Object):
    pass


class AdventuresLeaderboards(BaseAPIv2Object):
    pass


class AdventuresIdLeaderboards(BaseAPIv2Object):
    
    def get(self, id, **kwargs):
        board = kwargs.get('board')
        region = kwargs.get('region')
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)
        if board:
            endpoint_url += f'/{board}'
        if region:
            endpoint_url += f'/{region}'

        return super().get(url=endpoint_url)


class BackstoryAnswers(BaseAPIv2Object):
    pass


class BackstoryQuestions(BaseAPIv2Object):
    pass


class Build(BaseAPIv2Object):
    pass


class Cats(BaseAPIv2Object):
    pass


class Characters(BaseAPIv2Object):
    pass


class CharactersIdBackstory(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdCore(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)
    
class CharactersIdBuildTabs(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdBuildTabsActive(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdCrafting(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdDungeons(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdEquipment(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdHeropoints(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)

class CharactersIdEquipmentTabs(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdEquipmentTabsActive(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdHeroPoints(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdInventory(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdQuests(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdRecipes(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdSAB(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdSkills(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdSpecializations(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class CharactersIdTraining(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class Colors(BaseAPIv2Object):
    pass


class CommerceDelivery(BaseAPIv2Object):
    pass


class CommerceExchange(BaseAPIv2Object):
    pass


class CommerceExchangeCoins(BaseAPIv2Object):
    """Returns the current coins to gems exchange rate"""

    def get(self, quantity):
        """Returns the current coins to gems exchange rate

        Args:
            quantity: The number of coins to convert to gems

        Returns:
            The JSON response
        """

        endpoint_url = self._build_endpoint_base_url()
        endpoint_url += "?quantity=" + str(quantity)

        return super().get(url=endpoint_url)


class CommerceExchangeGems(BaseAPIv2Object):
    """Returns the current gems to coins exchange rate"""

    def get(self, quantity):
        """Returns the current gems to coins exchange rate

        Args:
            quantity: The number of gems to convert to coins

        Returns:
            The JSON response
        """

        endpoint_url = self._build_endpoint_base_url()
        endpoint_url += "?quantity=" + str(quantity)

        return super().get(url=endpoint_url)


class CommerceListings(BaseAPIv2Object):
    pass


class CommercePrices(BaseAPIv2Object):
    pass


class CommerceTransactions(BaseAPIv2Object):
    """Returns information on an account's past and current trading post transactions"""
    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, val):
        self._session = val
        self.history.session = val
        self.current.session = val
        self.history.buys.session = val
        self.history.sells.session = val
        self.current.buys.session = val
        self.current.sells.session = val

    def __init__(self, object_type):
        """
        Initializes a CommerceTransactions API object. See BaseAPIObject's __init__ documentation

        :param object_type: String indicating what type of object to
                             interface with (i.e. 'guild'). Primarily
                             acts as the relative path to the base URL
        :raises ValueError: In the event that either a `Session` object
                             or `object_type` are not set.
        """

        self._session = None

        # create second-level endpoints
        self.history = BaseAPIv2Object(object_type + "/history")
        self.current = BaseAPIv2Object(object_type + "/current")

        # create third-level endpoints
        self.history.buys = BaseAPIv2Object(self.history.object_type + "/buys")
        self.history.sells = BaseAPIv2Object(self.history.object_type + "/sells")
        self.current.buys = BaseAPIv2Object(self.current.object_type + "/buys")
        self.current.sells = BaseAPIv2Object(self.current.object_type + "/sells")

        super().__init__(object_type)


class Continents(BaseAPIv2Object):

    def _validate_kwargs(self, **kwargs):
        """Validates the keyword arguments.

        Since the continents endpoint is hierarchical, each level is dependent
        on its predecessor.

        Hence, the validation checks for the leaf supplied and walks up the
        tree to see if
        1. any higher level is missing
        2. any higher level supplies multiple ids
        In either case, a KeyError is raised.

        Special care is taken of the 'id' and 'ids' keywords, as those
        are synonymous for continents.

        Args:
            kwargs: The keyword arguments to validate.

        Raises:
            KeyError: if any needed level is missing, or any non-leaf level
            provides multiple IDs.
        """
        def raise_for_non_int(value):
            try:
                int(str(value))
            except ValueError:
                raise KeyError('too many ids supplied for {}'.format(level))

        levels = ['sectors', 'maps', 'regions', 'floors', 'continents']
        for i, current_level in enumerate(levels):
            if current_level in kwargs:
                for level in reversed(levels[i+1:]):  # All higher levels
                    if level not in kwargs:  # Check if level is supplied
                        if level != 'continents':  # Backwards compatibility for ids
                            raise KeyError('Please provide the {} key.'.format(level))
                        else:
                            if 'id' not in kwargs:
                                raise KeyError('Please provide the continents key.')
                    else:  # Check if no higher level supplies multiple IDs
                        if level != 'continents':
                            raise_for_non_int(kwargs.get(level))
                        else:  # Backwards compatibility for ids
                            value = kwargs.get(level) or kwargs.get('ids')
                            raise_for_non_int(value)

    def get(self, **kwargs):
        """Gets the continents resource.

        This resource is slightly different than other API resources, hence
        its differs slightly. Instead of using the id and ids attributes,
        this resource can walk along several levels:
            continents, floors, regions, maps, sectors

        For each layer, individual (single) IDs can be specified.
        For the leaf layer, i.e. the last specified layer, multiple IDs
        can be specified.

        If one layer is specified, all previous layers must be specified, too.
        For example, if specifying regions=38, then floors and continents need
        to be supplied, too.

        Args:
            kwargs: Can be any combination of
                    - continents
                    - floors
                    - regions
                    - maps
                    - sectors
                    With values being either single ints (ids), lists of ints,
                    or strings. A special case is 'all', which can be used
                    to get a list of all ids in a subresource.
        Returns:
            The JSON response.

        Raises:
            KeyError: if the validation of the keyword arguments fails.
        """
        request_url = self._build_endpoint_base_url()

        self._validate_kwargs(**kwargs)

        _id = kwargs.get('id')
        ids = kwargs.get('ids')
        continents = kwargs.get('continents') or ids or _id
        floors = kwargs.get('floors')
        regions = kwargs.get('regions')
        maps = kwargs.get('maps')
        sectors = kwargs.get('sectors')

        def id_string(value_or_values):
            if value_or_values == 'all':
                return ''
            if isinstance(value_or_values, str):
                if ',' in value_or_values:
                    return '?ids=' + value_or_values
                return '/' + value_or_values
            try:
                return '?ids=' + ','.join(map(str, value_or_values))
            except TypeError:  # single values are not iterable
                return '/' + str(value_or_values)

        # Since we validate before, we just have to build the url in order
        # not nested
        if continents:
            request_url += id_string(continents)
        if floors:
            request_url += '/floors' + id_string(floors)
        if regions:
            request_url += '/regions' + id_string(regions)
        if maps:
            request_url += '/maps' + id_string(maps)
        if sectors:
            request_url += '/sectors' + id_string(sectors)

        return super().get(url=request_url)


class CreateSubToken(BaseAPIv2Object):

    def get(self, expire, permissions, **kwargs):

        urls = kwargs.get('urls')

        endpoint_url = self._build_endpoint_base_url()
        endpoint_url += f'?expire={expire}&'
        endpoint_url += f'permissions={permissions}&'
        if urls:
            endpoint_url += f'urls={urls}'
        endpoint_url.rstrip('&')

        return super().get(url=endpoint_url)


class Currencies(BaseAPIv2Object):
    pass


class DailyCrafting(BaseAPIv2Object):
    pass


class Dungeons(BaseAPIv2Object):
    pass


class Emblem(BaseAPIv2Object):
    pass


class EmblemBackgrounds(BaseAPIv2Object):
    pass


class EmblemForegrounds(BaseAPIv2Object):
    pass


class Emotes(BaseAPIv2Object):
    pass


class Events(BaseAPIv2Object):
    pass


class EventsState(BaseAPIv2Object):
    pass


class Files(BaseAPIv2Object):
    pass


class Finishers(BaseAPIv2Object):
    pass


class GemstoreCatalog(BaseAPIv2Object):
    pass


class Gliders(BaseAPIv2Object):
    pass


class GuildId(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdLog(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdMembers(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdRanks(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdStash(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdStorage(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdTeams(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdTreasury(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdUpgrades(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildPermissions(BaseAPIv2Object):
    pass


class GuildSearch(BaseAPIv2Object):

    def get(self, name, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url += '?name={name}'.format(name=name)

        return super().get(url=endpoint_url)


class GuildUpgrades(BaseAPIv2Object):
    pass


class Home(BaseAPIv2Object):
    pass


class HomeCats(BaseAPIv2Object):
    pass


class HomeNodes(BaseAPIv2Object):
    pass


class Items(BaseAPIv2Object):
    pass


class ItemStats(BaseAPIv2Object):
    pass


class Legends(BaseAPIv2Object):
    pass


class MailCarriers(BaseAPIv2Object):
    pass


class Mapchests(BaseAPIv2Object):

    pass


class Maps(BaseAPIv2Object):
    pass


class Masteries(BaseAPIv2Object):
    pass


class Materials(BaseAPIv2Object):
    pass


class Minis(BaseAPIv2Object):
    pass


class Mounts(BaseAPIv2Object):
    pass


class MountsSkins(BaseAPIv2Object):
    pass


class MountsTypes(BaseAPIv2Object):
    pass


class Nodes(BaseAPIv2Object):
    pass


class Novelties(BaseAPIv2Object):
    pass


class Outfits(BaseAPIv2Object):
    pass


class Pets(BaseAPIv2Object):
    pass


class Professions(BaseAPIv2Object):
    pass


class PvP(BaseAPIv2Object):
    pass


class PvPAmulets(BaseAPIv2Object):
    pass


class PvPGames(BaseAPIv2Object):
    pass


class PvPHeroes(BaseAPIv2Object):
    pass


class PvPRanks(BaseAPIv2Object):
    pass


class PvPRewardTracks(BaseAPIv2Object):
    pass


class PvPRunes(BaseAPIv2Object):
    pass


class PvPSeasons(BaseAPIv2Object):
    pass


class PvPSeasonsLeaderboards(BaseAPIv2Object):
    pass


class PvPSeasonsIdLeaderboards(BaseAPIv2Object):

    def get(self, id, **kwargs):
        board = kwargs.get('board')
        region = kwargs.get('region')
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)
        if board:
            endpoint_url += f'/{board}'
        if region:
            endpoint_url += f'/{region}'

        return super().get(url=endpoint_url)


class PvPSigils(BaseAPIv2Object):
    pass


class PvPStandings(BaseAPIv2Object):
    pass


class PvPStats(BaseAPIv2Object):
    pass


class Quaggans(BaseAPIv2Object):
    pass


class Quests(BaseAPIv2Object):
    pass


class Races(BaseAPIv2Object):
    pass


class Raids(BaseAPIv2Object):
    pass


class Recipes(BaseAPIv2Object):
    pass


class RecipesSearch(BaseAPIv2Object):

    def get(self, **kwargs):
        if any(key in ['input', 'output'] for key in kwargs):
            param = 'input' if 'input' in kwargs else 'output'
            item_id = kwargs.get(param)

            endpoint_url = self._build_endpoint_base_url()
            endpoint_url += '?{param}={item_id}'.format(param=param, item_id=item_id)

            return super().get(url=endpoint_url)

        # Fallback to let the official API handle the error cases
        return super().get(**kwargs)


class Skills(BaseAPIv2Object):
    pass


class Skins(BaseAPIv2Object):
    pass


class Specializations(BaseAPIv2Object):
    pass


class Stories(BaseAPIv2Object):
    pass


class StoriesSeasons(BaseAPIv2Object):
    pass


class Titles(BaseAPIv2Object):
    pass


class Tokeninfo(BaseAPIv2Object):
    pass


class Traits(BaseAPIv2Object):
    pass


class Vendors(BaseAPIv2Object):
    pass


class Worlds(BaseAPIv2Object):
    pass


class WorldBosses(BaseAPIv2Object):
    pass


class Wvw(BaseAPIv2Object):
    pass


class WvwAbilities(BaseAPIv2Object):
    pass


class WvwMatches(BaseAPIv2Object):
    pass


class WvwMatchesOverview(BaseAPIv2Object):
    pass


class WvwMatchesScores(BaseAPIv2Object):
    pass


class WvwMatchesStatsTeams(BaseAPIv2Object):
    pass


class WvwMatchesStats(BaseAPIv2Object):

    def get(self, match_id=None):
        endpoint_url = self._build_endpoint_base_url()
        if match_id:
            endpoint_url += f'/{match_id}'

        return super().get(url=endpoint_url)


class WvwMatchesStatsGuilds(BaseAPIv2Object):

    def get(self, match_id, guild_id):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', match_id)
        endpoint_url = endpoint_url.replace(':guild_id', guild_id)

        return super().get(url=endpoint_url)


class WvwMatchesStatsTeamsTopKDR(BaseAPIv2Object):

    def get(self, match_id, team):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', match_id)
        endpoint_url = endpoint_url.replace(':team', team)

        return super().get(url=endpoint_url)


class WvwMatchesStatsTeamsTopKills(BaseAPIv2Object):

    def get(self, match_id, team):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', match_id)
        endpoint_url = endpoint_url.replace(':team', team)

        return super().get(url=endpoint_url)


class WvwObjectives(BaseAPIv2Object):
    pass


class WvwRanks(BaseAPIv2Object):
    pass


class WvwRewardTracks(BaseAPIv2Object):
    pass


class WvwUpgrades(BaseAPIv2Object):
    pass


API_OBJECTS = [Account('account'),
               AccountAchievements('account/achievements'),
               AccountBank('account/bank'),
               AccountBuildStorage('account/buildstorage'),
               AccountDailyCrafting('account/dailycrafting'),
               AccountDungeons('account/dungeons'),
               AccountDyes('account/dyes'),
               AccountEmotes('account/emotes'),
               AccountFinishers('account/finishers'),
               AccountGliders('account/gliders'),
               AccountHome('account/home'),
               AccountHomeCats('account/home/cats'),
               AccountHomeNodes('account/home/nodes'),
               AccountInventory('account/inventory'),
               AccountLuck('account/luck'),
               AccountMail('account/mail'),
               AccountMailCarriers('account/mailcarriers'),
               AccountMapChests('account/mapchests'),
               AccountMasteries('account/masteries'),
               AccountMasteryPoints('account/mastery/points'),
               AccountMaterials('account/materials'),
               AccountMinis('account/minis'),
               AccountMounts('account/mounts'),
               AccountMountsSkins('account/mounts/skins'),
               AccountMountsTypes('account/mounts/types'),
               AccountNovelties('account/novelties'),
               AccountOutfits('account/outfits'),
               AccountPvPHeroes('account/pvp/heroes'),
               AccountRaids('account/raids'),
               AccountRecipes('account/recipes'),
               AccountSkins('account/skins'),
               AccountTitles('account/titles'),
               AccountWallet('account/wallet'),
               AccountWorldBosses('account/worldbosses'),
               Achievements('achievements'),
               AchievementsCategories('achievements/categories'),
               AchievementsDaily('achievements/daily'),
               AchievementsDailyTomorrow('achievements/daily/tomorrow'),
               AchievementsGroups('achievements/groups'),
               Adventures('adventures'),
               AdventuresLeaderboards('adventures/:id/leaderboards'),
               AdventuresIdLeaderboards('adventures/:id/leaderboards/:board/:region'),
               BackstoryAnswers('backstory/answers'),
               BackstoryQuestions('backstory/questions'),
               Build('build'),
               Cats('cats'),
               Characters('characters'),
               CharactersIdBackstory('characters/:id/backstory'),
               CharactersIdBuildTabs('characters/:id/buildtabs'),
               CharactersIdBuildTabsActive('characters/:id/buildtabs/active'),
               CharactersIdCore('characters/:id/core'),
               CharactersIdCrafting('characters/:id/crafting'),
               CharactersIdDungeons('characters/:id/dungeons'),
               CharactersIdEquipment('characters/:id/equipment'),
               CharactersIdEquipmentTabs('characters/:id/equipmenttabs'),
               CharactersIdEquipmentTabsActive('characters/:id/equipmenttabs/active'),
               CharactersIdHeroPoints('characters/:id/heropoints'),
               CharactersIdInventory('characters/:id/inventory'),
               CharactersIdQuests('characters/:id/quests'),
               CharactersIdRecipes('characters/:id/recipes'),
               CharactersIdSAB('characters/:id/sab'),
               CharactersIdSkills('characters/:id/skills'),
               CharactersIdSpecializations('characters/:id/specializations'),
               CharactersIdTraining('characters/:id/training'),
               Colors('colors'),
               CommerceDelivery('commerce/delivery'),
               CommerceExchange('commerce/exchange'),
               CommerceExchangeCoins('commerce/exchange/coins'),
               CommerceExchangeGems('commerce/exchange/gems'),
               CommerceListings('commerce/listings'),
               CommercePrices('commerce/prices'),
               CommerceTransactions('commerce/transactions'),
               Continents('continents'),
               CreateSubToken('createsubtoken'),
               Currencies('currencies'),
               DailyCrafting('dailycrafting'),
               Dungeons('dungeons'),
               Emblem('emblem'),
               EmblemBackgrounds('emblem/backgrounds'),
               EmblemForegrounds('emblem/foregrounds'),
               Emotes('emotes'),
               Events('events'),
               EventsState('events-state'),
               Files('files'),
               Finishers('finishers'),
               GemstoreCatalog('gemstore/catalog'),
               Gliders('gliders'),
               GuildId('guild/:id'),
               GuildIdLog('guild/:id/log'),
               GuildIdMembers('guild/:id/members'),
               GuildIdRanks('guild/:id/ranks'),
               GuildIdStash('guild/:id/stash'),
               GuildIdStorage('guild/:id/storage'),
               GuildIdTeams('guild/:id/teams'),
               GuildIdTreasury('guild/:id/treasury'),
               GuildIdUpgrades('guild/:id/upgrades'),
               GuildPermissions('guild/permissions'),
               GuildSearch('guild/search'),
               GuildUpgrades('guild/upgrades'),
               Home('home'),
               HomeCats('home/cats'),
               HomeNodes('home/nodes'),
               Items('items'),
               ItemStats('itemstats'),
               Legends('legends'),
               MailCarriers('mailcarriers'),
               Mapchests('mapchests'),
               Maps('maps'),
               Masteries('masteries'),
               Materials('materials'),
               Minis('minis'),
               Mounts('mounts'),
               MountsSkins('mounts/skins'),
               MountsTypes('mounts/types'),
               Nodes('nodes'),
               Novelties('novelties'),
               Outfits('outfits'),
               Pets('pets'),
               Professions('professions'),
               PvP('pvp'),
               PvPAmulets('pvp/amulets'),
               PvPGames('pvp/games'),
               PvPHeroes('pvp/heroes'),
               PvPRanks('pvp/ranks'),
               PvPRewardTracks('pvp/rewardtracks'),
               PvPRunes('pvp/runes'),
               PvPSeasons('pvp/seasons'),
               PvPSeasonsLeaderboards('pvp/seasons/leaderboards'),
               PvPSeasonsIdLeaderboards('pvp/seasons/:id/leaderboards'),
               PvPSigils('pvp/sigils'),
               PvPStandings('pvp/standings'),
               PvPStats('pvp/stats'),
               Quaggans('quaggans'),
               Quests('quests'),
               Races('races'),
               Raids('raids'),
               Recipes('recipes'),
               RecipesSearch('recipes/search'),
               Skills('skills'),
               Skins('skins'),
               Specializations('specializations'),
               Stories('stories'),
               StoriesSeasons('stories/seasons'),
               Titles('titles'),
               Tokeninfo('tokeninfo'),
               Traits('traits'),
               Vendors('vendors'),
               WorldBosses('worldbosses'),
               Worlds('worlds'),
               Wvw('wvw'), 
               WvwAbilities('wvw/abilities'),
               WvwMatches('wvw/matches'),
               WvwMatchesOverview('wvw/matches/overview'),
               WvwMatchesScores('wvw/matches/scores'),
               WvwMatchesStats('wvw/matches/stats'),
               WvwMatchesStatsGuilds('wvw/matches/stats/:id/guilds/:guild_id'),
               WvwMatchesStatsTeams('wvw/matches/stats/teams'),
               WvwMatchesStatsTeamsTopKDR('wvw/matches/stats/:id/teams/:team/top/kdr'),
               WvwMatchesStatsTeamsTopKills('wvw/matches/stats/:id/teams/:team/top/kills'),
               WvwObjectives('wvw/objectives'),
               WvwRanks('wvw/ranks'),
               WvwRewardTracks('wvw/rewardtracks'),
               WvwUpgrades('wvw/upgrades')]
