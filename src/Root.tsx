import React from 'react';
import {Composition} from 'remotion';
import {DioramaShort} from '../templates/diorama/DioramaShort';
import {FPS, TOTAL} from '../templates/diorama/story';

export const Root: React.FC = () => <Composition
  id="DioramaShort" component={DioramaShort} width={1080} height={1920}
  fps={FPS} durationInFrames={TOTAL}
  defaultProps={{captions: true, labels: true, title: 'WATER NEEDS A PATH', voice: null}}
/>;
