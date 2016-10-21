class SongCollection(object):

    def __init__(self, songs):
        assert isinstance(songs, list)
        self.songs = songs

    def total_time(self):
        return sum(s.duration for s in self.songs)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return "A collection with %d songs" % len(self)

    def __nonzero__(self):
        return False

    def __getitem__(self, num):
        return self.songs[num]

    def __iter__(self):
        return iter([1,2,3,4])
