from pydub import effects
from src.pipelines.audio.audio_processor_base import AudioProcessorBase
from src.utils.structlog_logger import StructLogger
from src.utils.performance_tracker import PerformanceTracker

logger = StructLogger.get_logger()
perf_tracker = PerformanceTracker.get_instance()


class AudioNormalizer(AudioProcessorBase):
    def normalize(self, input_file, output_file):
        try:
            audio = self.load_audio(input_file)
            normalized_audio = effects.normalize(audio)
            return self.save_audio(normalized_audio, output_file)
        except Exception as e:
            logger.error(f"Error normalizing audio file {input_file}: {e}")
            raise
