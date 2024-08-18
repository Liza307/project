/* eslint-disable */
import {
  Avatar,
  Badge,
  Card,
  ConfigProvider,
  Divider,
  Flex,
  Layout,
  Tag,
  Tooltip,
} from "antd";
import "./Profile.css";
import { useState } from "react";
import { PROFILE, PROFILE_COMPANY } from "../../mocks/user-data";
import Text from "antd/lib/typography/Text";
import { AntDesignOutlined, UserOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";
import { OrganizationChart } from "primereact/organizationchart";
import { nodeTemplate } from "../../components/Tree/Tree";
import PhoneIcon from "../../assets/images/phone_icon.svg";
import TelegramIcon from "../../assets/images/telegram_icon.svg";
import MailIcon from "../../assets/images/mail_icon.svg";
import StatusIcon from "../../assets/images/status_icon.png";

function Profile() {
  const [profile, setProfile] = useState(PROFILE);
  const [selection, setSelection] = useState([]);

  return (
    <Layout
      style={{
        height: "calc(100vh - 48px)",
        overflowY: "scroll",
      }}
    >
      <Flex
        style={{
          padding: 24,
          gap: 24,
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 24,
            marginTop: 20,
          }}
        >
          <Card
            style={{
              width: 368,
              display: "flex",
              flexDirection: "column",
              borderRadius: 0,
            }}
          >
            <div style={{ display: "flex", flexDirection: "column" }}>
              <img
                src={profile.avatar}
                alt="Аватар"
                style={{
                  width: 125,
                  height: 125,
                  margin: "auto",
                }}
              ></img>
              <Text
                style={{
                  margin: "24px 0",
                  fontSize: 20,
                  fontWeight: 500,
                  lineHeight: "28px",
                  textOverflow: "ellipsis",
                }}
              >
                {profile.name}
              </Text>
              <Text>{profile.job}</Text>
              <Text>{profile.city}</Text>
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  marginTop: 24,
                }}
              >
                <img
                  src={StatusIcon}
                  alt="Icon"
                  style={{
                    width: 12,
                    height: 12,
                  }}
                ></img>
                <Text
                  style={{
                    marginLeft: 10,
                  }}
                >
                  {profile.status}
                </Text>
              </div>
              <Divider></Divider>
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  gap: 22,
                }}
              >
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                  }}
                >
                  <img
                    src={MailIcon}
                    alt="Icon"
                    style={{
                      width: 16,
                      height: 16,
                    }}
                  ></img>
                  <Text
                    style={{
                      color: "#1890FF",
                      marginLeft: 16,
                    }}
                  >
                    {profile.email}
                  </Text>
                </div>
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                  }}
                >
                  <img
                    src={PhoneIcon}
                    alt="Icon"
                    style={{
                      width: 16,
                      height: 16,
                    }}
                  ></img>
                  <Text
                    style={{
                      color: "#1890FF",
                      marginLeft: 16,
                    }}
                  >
                    {profile.phone}
                  </Text>
                </div>
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                  }}
                >
                  <img
                    src={TelegramIcon}
                    alt="Icon"
                    style={{
                      width: 16,
                      height: 16,
                    }}
                  ></img>
                  <Text
                    style={{
                      color: "#1890FF",
                      marginLeft: 16,
                    }}
                  >
                    {profile.telegram}
                  </Text>
                </div>
              </div>
            </div>
          </Card>
          <Card title="Проекты" style={{ width: 368, borderRadius: 0 }}>
            <ConfigProvider>
              <Flex
                gap="middle"
                style={{
                  flexWrap: "wrap",
                }}
              >
                {profile.projects.map((project) => (
                  <Card
                    title={project.title}
                    size="small"
                    className="card__title"
                    style={{
                      width: 320,
                      height: 212,
                      borderRadius: 0,
                      overflow: "hidden",
                    }}
                  >
                    <div className="card__data">
                      <Text
                        style={{
                          textOverflow: "ellipsis",
                          maxWidth: "288px",
                        }}
                        className="card__more"
                      >
                        {project.description}
                      </Text>
                      <Flex
                        gap="12px 0"
                        wrap
                        style={{
                          margin: "12px 0 4px",
                        }}
                      >
                        {project.tags.map((item) => (
                          <Tag color="purple">{item.name}</Tag>
                        ))}
                      </Flex>
                      <div
                        style={{
                          flexDirection: "row",
                          width: "100%",
                        }}
                        className="card__projects"
                      >
                        <Link
                          style={{
                            color: "#1890FF",
                          }}
                          to={""}
                        >
                          Подчиненные проекты
                        </Link>
                        <Badge
                          className="card__badge"
                          count={project.project_value}
                          style={{
                            backgroundColor: "#FFF",
                            color: "#1890FF",
                            fontWeight: "500",
                            fontSize: "14px",
                            lineHeight: "24px",
                          }}
                        ></Badge>
                      </div>
                      <div
                        style={{
                          margin: "6px 0 4px",
                        }}
                      >
                        <Text
                          style={{
                            fontSize: "14px",
                            fontWeight: "500",
                            marginRight: "5px",
                          }}
                        >
                          Сотрудники
                        </Text>
                        <Text
                          style={{
                            fontSize: "14px",
                            fontWeight: "500",
                          }}
                        >
                          {project.worker_value}
                        </Text>
                      </div>
                      <Avatar.Group
                        size="large"
                        max={{
                          count: 4,
                          style: {
                            color: "#f56a00",
                            backgroundColor: "#fde3cf",
                            cursor: "pointer",
                          },
                          popover: {
                            trigger: "click",
                          },
                        }}
                      >
                        <Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
                        <Avatar
                          style={{
                            backgroundColor: "#f56a00",
                          }}
                        >
                          K
                        </Avatar>
                        <Tooltip title="Ant User" placement="top">
                          <Avatar
                            style={{
                              backgroundColor: "#87d068",
                            }}
                            icon={<UserOutlined />}
                          />
                        </Tooltip>
                        <Avatar
                          style={{
                            backgroundColor: "#1677ff",
                          }}
                          icon={<AntDesignOutlined />}
                        />
                        <Avatar
                          style={{
                            backgroundColor: "#1677ff",
                          }}
                          icon={<AntDesignOutlined />}
                        />
                      </Avatar.Group>
                    </div>
                  </Card>
                ))}
              </Flex>
            </ConfigProvider>
          </Card>
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 24,
          }}
        >
          <Card
            title="Общая информация"
            style={{ width: 792, borderRadius: 0 }}
          >
            <div
              style={{
                display: "flex",
              }}
            >
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  maxWidth: 149,
                  marginRight: 16,
                  gap: 16,
                  opacity: 0.45,
                }}
              >
                <Text>Департамент:</Text>
                <Text>Отдел:</Text>
                <Text>Часовой пояс:</Text>
                <Text>О себе:</Text>
                <Text>Следующий отпуск:</Text>
                <Text>Навыки:</Text>
                <Text>Тип найма:</Text>
              </div>
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  gap: 16,
                }}
              >
                <Text>IT</Text>
                <Text>Отдел мобильной разработки</Text>
                <Text>UTC+3</Text>
                <Text>С 2022 года работаю в N</Text>
                <Text>22.06.2025 — 09.07.2025</Text>
                <div>
                  <Tag>Python</Tag>
                  <Tag>Python</Tag>
                  <Tag>Python</Tag>
                </div>
                <Text>Штатный</Text>
              </div>
            </div>
          </Card>
          <Card
            title="Организация"
            style={{ width: 792, overflow: "auto", borderRadius: 0 }}
          >
            <OrganizationChart
              value={PROFILE_COMPANY}
              selectionMode="multiple"
              selection={selection}
              onSelectionChange={(e) => setSelection(e.data)}
              nodeTemplate={nodeTemplate}
            ></OrganizationChart>
          </Card>
        </div>
      </Flex>
    </Layout>
  );
}

export default Profile;
