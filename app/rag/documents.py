from dataclasses import dataclass


@dataclass(frozen=True)
class MusicDocument:
    id: int
    artist: str
    title: str
    genre: list[str]
    mood: list[str]
    description: str


MUSIC_DOCUMENTS = [
    MusicDocument(
        id=1,
        artist="She Past Away",
        title="Ritüel",
        genre=["darkwave", "post-punk"],
        mood=["dark", "hypnotic", "melancholic"],
        description=(
            "A hypnotic darkwave track with driving bass, "
            "minimal synth textures, post-punk guitar, and "
            "a dark ritualistic atmosphere."
        ),
    ),
    MusicDocument(
        id=2,
        artist="Boy Harsher",
        title="Pain",
        genre=["darkwave", "minimal synth"],
        mood=["dark", "sensual", "hypnotic"],
        description=(
            "A minimal synth and darkwave track built around "
            "pulsing electronic rhythms and haunting vocals."
        ),
    ),
    MusicDocument(
        id=3,
        artist="Molchat Doma",
        title="Sudno",
        genre=["post-punk", "coldwave"],
        mood=["melancholic", "dark", "minimal"],
        description=(
            "A coldwave-inspired post-punk track with repetitive "
            "bass, restrained vocals, and a bleak atmosphere."
        ),
    ),
    MusicDocument(
        id=4,
        artist="Lebanon Hanover",
        title="Gallowdance",
        genre=["minimal wave", "post-punk"],
        mood=["dark", "melancholic", "danceable"],
        description=(
            "A minimalist post-punk track combining repetitive "
            "bass lines, detached vocals, and a danceable rhythm."
        ),
    ),
    MusicDocument(
        id=5,
        artist="Twin Tribes",
        title="Heart & Soul",
        genre=["darkwave", "post-punk"],
        mood=["romantic", "dark", "dreamy"],
        description=(
            "A modern darkwave track with atmospheric synths, "
            "melodic bass, and dreamy vocals."
        ),
    ),
]