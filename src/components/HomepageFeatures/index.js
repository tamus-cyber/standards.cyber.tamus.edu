import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Control Standards Catalog',
    Svg: require('@site/static/img/undraw-books.svg').default,
    description: (
      <>
        The Control Standards Catalog includes minimum information security requirements for all members’ information and information resources.
      </>
    ),
  },
  {
    title: 'Guidelines',
    Svg: require('@site/static/img/undraw-directions.svg').default,
    description: (
      <>
        Guidelines provide enhanced direction to system members for implementing the security control standards established by the control standards catalog.
      </>
    ),
  },
  {
    title: 'Resources',
    Svg: require('@site/static/img/undraw-helpful-sign.svg').default,
    description: (
      <>
        Resources are available to assist system members in their implementation of cybersecurity standards.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
